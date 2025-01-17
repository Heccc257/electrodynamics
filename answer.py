import json
import argparse
import os 
from tqdm import tqdm
import torch
from vllm import LLM, SamplingParams

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

def post_process(input, answer):
    length = len(input)
    if answer[0: length] == input:
        answer = answer[length: ]
    return answer

def apply_system_template(prompt):
    template = f'''<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
{prompt} <|im_end|>
    '''
    return template

def get_answers(
    model_path,
    # model=None,
    # tokenizer=None,
    datasets=None,
    output_dir=None,
    prompt_template=None,
):

    print(f"prompt template: {prompt_template}")
    llm = LLM(
        model=model_path,
        max_model_len=1024,
    )

    sampling_params = SamplingParams(
        max_tokens=1024,  # 生成的最大新token数，包括输入文本
        best_of=3,
        n=1,  # 返回的序列数量
        temperature=0.7,  # 控制输出的随机性，值越低输出越确定但可能更单调
        top_p=0.9,  # 核采样，只从累积概率最高的词汇中选择下一个token
        top_k=50,  # Top-k采样，只从概率最高的k个词汇中选择下一个token
        repetition_penalty=1.2  # 对已经生成过的token施加惩罚，以降低其再次被选中的概率
    )
    
    for dataset in datasets:
        print("=====================")
        print(f"begin answer dataset: {dataset}")
        answers = []

        data_name = dataset.split('/')[-1]
        output_path = os.path.join(output_dir, "answer_" + data_name)
        
        data = json.load(open(dataset, "r"))
        for idx, json_obj in enumerate(tqdm(data)):
            if (len(json_obj.keys())) < 2:
                print(json_obj["input"])
                continue

            # 根据template构造完整得prompt
            prompt = prompt_template.format(**json_obj)
            prompt = apply_system_template(prompt)

            if idx == 0:
                print("===== prompt example =====")
                print(prompt)
                print("")

            outputs = llm.generate(prompt, sampling_params=sampling_params)
            generated_text = outputs[0].outputs[0].text

            # generated_text = post_process(prompt, generated_text)
            
            answer = {}
            answer["input"] = json_obj["input"]
            answer["standard"] = json_obj["output"]
            answer["output"] = generated_text

            answers.append(answer)
            
            if idx%10 == 0 or idx < 5:
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

    # model, tokenizer = load_model_and_tokenizer(model_path)

    prompt_type = args.prompt
    print(f"prompt type {prompt_type}")
    prompts = json.load(open("config/prompt.json", 'r'))
    prompt = prompts[prompt_type]

    get_answers(model_path=model_path, 
        datasets=datasets, output_dir=output_dir, prompt_template=prompt)

