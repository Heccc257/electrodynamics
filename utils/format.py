import json

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
        f.write(json_str)


dataset = json.load(open("datasets/training_data/cot/cot_textbook.json", "r"))
dataset = dataset[0: 10]
for idx in range(len(dataset)):
    data = dataset[idx]
    if r"\\\\" in repr(data["output"]):
        raw_str = data["output"]
        # print(raw_str)
        # print("")
        raw_str = raw_str.replace("\\\\", "\\")
        # print(raw_str)
        # exit(0)
        dataset[idx]["output"] = raw_str

save_json(dataset, "datasets/raw.json")