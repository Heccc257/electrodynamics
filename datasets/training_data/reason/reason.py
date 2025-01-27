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

prompt = r"""下面将给出一个电动力学问题请, 给出对应的思考过程即可。
    要求解答要尽量简洁，最好不要超过4096个token，每个步骤用<|>分割。
    注意公式使用$$并且关键字前使用\\,比如$\\sum_i$, $\\frac a b $ 
    例如：```
    input："在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式是如何与加速度的平行和垂直分量相关的？"
    output："<|>在相对论粒子的辐射中，电场 $\\\\boldsymbol{E}$ 的表达式可以通过粒子的加速度 $\\\\boldsymbol{a}$ 的平行和垂直分量来描述。<|>首先，粒子的加速度 $\\\\boldsymbol{a}$ 可以分解为平行于速度 $\\\\boldsymbol{v}$ 的分量 $\\\\boldsymbol{a}_\\\\parallel$ 和垂直于速度 $\\\\boldsymbol{v}$ 的分量 $\\\\boldsymbol{a}_\\\\perp$。<|>..."
    ```

    下面是问题：\n

"""

output_dir = "datasets/training_data/reason"
output_path = os.path.join(output_dir, file.split('/')[-1])
print(f"file: {file}")
print(f"output_dir: {output_path}")

outputs = []
for data in datasets:
    outputs.append({
        "instruction": prompt,
        "input": data["instruction"],
        "output": data["cot"],
    })

save_json(outputs, output_path)