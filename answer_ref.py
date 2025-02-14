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

# def apply_system_template(prompt):
#     template = f'''<|im_start|>system
# You are a helpful assistant.<|im_end|>
# <|im_start|>user
# {prompt} <|im_end|>
#     '''
#     return template
def apply_system_template(prompt):
    template = f'''<｜begin▁of▁sentence｜>User:{prompt}
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
    prompts = json.load(open("config/prompt.json", 'r'))

    cot_prompt_template = "下面将给出一个电动力学问题以及参考答案，请一步一步思考，使用中文给出你自己的思考过程和解答，解答过程中不要提及参考答案。\n    要求思考过程详细，解答要尽量简洁,思考过程用<think></think>包裹,解答用<answer></answer>包裹\n    注意公式使用$$\n    例如：```\n    User: \"在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式是如何与加速度的平行和垂直分量相关的？\"\n    Assistant: \"<think>在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式可以通过粒子的加速度 $\\boldsymbol{a}$ 的平行和垂直分量来描述。...</think>\\n <answer>线性加速器中，粒子的速度 $\\mathbf{v}$ 与加速度 ...</answer>\"\n    ```\n    下面是问题和参考答案：\n\n"
    
    print(f"prompt template: {cot_prompt_template}")

    max_len = 1024*6
    llm = LLM(
        model=model_path,
        max_model_len=max_len,
    )

    sampling_params = SamplingParams(
        max_tokens=max_len,  # 生成的最大新token数，包括输入文本
        best_of=3,
        n=1,  # 返回的序列数量
        temperature=0.6,  # 控制输出的随机性，值越低输出越确定但可能更单调
        top_p=0.9,  # 核采样，只从累积概率最高的词汇中选择下一个token
        top_k=50,  # Top-k采样，只从概率最高的k个词汇中选择下一个token
        repetition_penalty=1.2  # 对已经生成过的token施加惩罚，以降低其再次被选中的概率
    )
    
    batch_size = 20
    
    for dataset in datasets:
        print("=====================")
        print(f"begin answer dataset: {dataset}")
        answers = []

        data_name = dataset.split('/')[-1]
        output_path = os.path.join(output_dir, "answer_" + data_name)
        
        data = json.load(open(dataset, "r"))
        data_batchs = [data[i: min(len(data), i+batch_size)] for i in range(0, len(data), batch_size)]
        
        for idx, json_objs in enumerate(tqdm(data_batchs)):
            
            cot_prompts = [cot_prompt_template + json_obj["input"] + "\n\n" + json_obj["output"] for json_obj in json_objs]
            cot_prompts = [apply_system_template(cot_prompt) for cot_prompt in cot_prompts]

            if idx == 0:
                print("===== prompt example =====")
                print(cot_prompts[0])
                print("")


            outputs = llm.generate(cot_prompts, sampling_params=sampling_params)

            for i in range(len(outputs)):
                json_obj = json_objs[i]
                response = outputs[i].outputs[0].text
                answer = {}
                answer["instruction"] = json_obj["input"]
                answer["standard"] = json_obj["output"] if "output" in json_obj.keys() else ""
                answer["output"] = response

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

