import json

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
        f.write(json_str)

data = json.load(open("datasets/cot_textbook.json", "r"))
data = data[::5]

save_json(data, output_path="datasets/sample_textbook.json")
