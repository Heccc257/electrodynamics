import json
import random

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
        f.write(json_str)

datas = json.load(open("datasets/basics/textbook.json", "r"))
random.shuffle(datas)

sample = []
for data in datas[: 50]:
    sample.append({
        "input": data["instruction"],
        "output": data["output"]
    })
save_json(sample, "sample_question.json")