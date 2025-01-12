import os
import json
import argparse

# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='这是一个简单的命令行工具示例')

# 添加位置参数（positional arguments）
parser.add_argument('--dir', type=str, help='输入文件目录')

args = parser.parse_args()
for file in os.listdir(args.dir):
    path = os.path.join(args.dir, file)
    print(path)
    data = json.load(open(path, "r"))
    alpaca = []
    for json_obj in data:
        if "output" not in json_obj.keys(): continue
        alpaca.append({
            "instruction": json_obj["input"],
            "input": "",
            "output": json_obj["output"]
        })
    json_str = json.dumps(alpaca, ensure_ascii=False, indent=4)
    with open(os.path.join("sft", file), "w", encoding="utf-8") as f:
            f.write(json_str)