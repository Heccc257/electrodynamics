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

prompt = r"""下面将给出一个电动力学问题以及对应的思考过程，请给出对应的解答。
    要求解答要尽量简洁，不需要给出思考过程。
    注意公式使用$$并且关键字前使用\\,比如$\\sum_i$, $\\frac a b $ 
    例如：```
    {
        "问题": "在镜像法中，电势 $\\widetilde{\\varphi}$ 的表达式是如何推导出来的？",
        "思考过程": "<|>在镜像法中，电势 $\\\\widetilde{\\\\varphi}$ 的推导基于以下步骤：<|>首先，考虑一个点电荷 $q$ 位于导体平面附近，导体平面接地，电势为零。<|>..."
    }

    output：电势 $\\widetilde{\\varphi}$ 的表达式是通过将原电荷 $q$ 和镜像电荷 $-q$ 的电势叠加得到的。具体来说，$\\widetilde{\\varphi}$ 是由 $q$ 和 $-q$ 分别在空间中产生的电势之和，即 $$\n\\widetilde{\\varphi}=\\frac{1}{4\\pi\\epsilon_{0}}\\left(\\frac{q}{\\sqrt{x^{2}+y^{2}+(z-d)^{2}}}-\\frac{q}{\\sqrt{x^{2}+y^{2}+(z+d)^{2}}}\\right).\n$$
    ```

    下面是问题和思考过程：\n

"""

output_dir = "datasets/training_data/answer"
output_path = os.path.join(output_dir, file.split('/')[-1])
print(f"file: {file}")
print(f"output_dir: {output_path}")

outputs = []
for data in datasets:
    outputs.append({
        "instruction": prompt,
        "input": json.dumps({"问题": data["instruction"], "思考过程": data["cot"]}, ensure_ascii=False, indent=4),
        "output": data["output"],
    })

save_json(outputs, output_path)