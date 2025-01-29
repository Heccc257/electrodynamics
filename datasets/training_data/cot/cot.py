import os
import argparse
import json

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
        f.write(json_str)

parser = argparse.ArgumentParser(description="Process a JSON file with electrodynamics problems.")
parser.add_argument("--file", type=str, help="Path to the JSON file containing the electrodynamics problems.")
args = parser.parse_args()

file = args.file

datasets = json.load(open(file, "r"))

prompt = "下面将给出一个电动力学问题，请一步一步思考，使用中文给出思考过程和解答。\n    要求思考过程详细，解答要尽量简洁,思考过程用<think></think>包裹,解答用<answer></answer>包裹\n    注意公式使用$$\n    例如：```\n    User: \"在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式是如何与加速度的平行和垂直分量相关的？\"\n    Assistant: \"<think>在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式可以通过粒子的加速度 $\\boldsymbol{a}$ 的平行和垂直分量来描述。...</think>\\n <answer>线性加速器中，粒子的速度 $\\mathbf{v}$ 与加速度 ...</answer>\"\n    ```\n    下面是问题：\n\n"

output_dir = "datasets/training_data/cot"
output_path = os.path.join(output_dir, file.split('/')[-1])
print(f"file: {file}")
print(f"output_dir: {output_path}")

outputs = []
for data in datasets:
    outputs.append({
        "instruction": prompt,
        "input": data["instruction"],
        "output": data["output"]
    })

save_json(outputs, output_path)