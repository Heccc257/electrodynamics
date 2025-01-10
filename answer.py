import json
import argparse
import os 
from tqdm import tqdm
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    GenerationConfig,
)


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        default="Qwen2-1.5B-Instruct",
    )

    parser.add_argument(
        "--data",
        type=str,
        default=None,
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        default="output"
    )

    parser.add_argument(
        "--prompt",
        type=str,
        help="prompt type",
        default="default",
    )
    return parser.parse_args(args)

def load_model_and_tokenizer(path):
    tokenizer = AutoTokenizer.from_pretrained(
        path, trust_remote_code=True, use_fast=False
    )
    model = AutoModelForCausalLM.from_pretrained(
        path,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
    ).eval()

    model = model.to("cuda")

    return model, tokenizer

def get_answers(
    model=None,
    tokenizer=None,
    datasets=None,
    output_dir=None,
    prompt_template=None,
):

    for dataset in datasets:
        print("=====================")
        print(f"begin answer dataset: {dataset}")
        answers = []

        data_name = dataset.split('/')[-1]
        output_path = os.path.join(output_dir, data_name)
        
        data = json.load(open(dataset, "r"))
        for idx, json_obj in enumerate(tqdm(data)):
            if (len(json_obj.keys())) < 2:
                print(json_obj["input"])
                continue

            # 根据template构造完整得prompt
            prompt = prompt_template.format(**json_obj)

            # 这部分后面可以换成vllm
            input_ids = tokenizer(
                prompt, return_tensors="pt"
            ).input_ids.to("cuda")

            output = model.generate(input_ids, max_length=500, num_return_sequences=1)
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
            print(f"generated_text {generated_text}")
            
            answer = {}
            answer["input"] = json_obj["input"]
            answer["standard"] = json_obj["output"]
            answer["output"] = generated_text

            answers.append(answer)
            
            if idx%10 == 0:
                json_str = json.dumps(answers, ensure_ascii=False, indent=4)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(json_str)

        print(f"output_path: {output_path}")
        json_str = json.dumps(answers, ensure_ascii=False, indent=4)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(json_str)

if __name__ == "__main__":
    args = parse_args()
    model_name = args.model
    data_name = args.data
    output_dir = args.output_dir

    output_dir = os.path.join(output_dir, model_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if os.path.isfile(data_name):
        datasets = [data_name]
    else:
        datasets = [os.path.join(data_name, name) for name in os.listdir(data_name)]

    print(f"datasets: {datasets}")
    model2path = json.load(open("config/model2path.json", 'r'))
    model_path = model2path[model_name]
    print(f"model name: {model_name}, model path: {model_path}")

    model, tokenizer = load_model_and_tokenizer(model_path)

    prompt_type = args.prompt
    print(prompt_type)
    prompts = json.load(open("config/prompt.json", 'r'))
    prompt = prompts[prompt_type]
    print(f"prompt: {prompt}")

    get_answers(model=model, tokenizer=tokenizer, 
        datasets=datasets, output_dir=output_dir, prompt_template=prompt)

