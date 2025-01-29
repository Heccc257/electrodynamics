import json
import argparse

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
        f.write(json_str)

parser = argparse.ArgumentParser(description="Process a JSON file with electrodynamics problems.")
parser.add_argument("--file", type=str, help="Path to the JSON file containing the electrodynamics problems.")

file = parser.parse_args().file

dataset = json.load(open(file, "r"))

median = "datasets/median.json"
hard = "datasets/hard.json"

median_dataset = []
hard_dataset = []

for data in dataset:
    if data["score"] < 5:
        hard_dataset.append(data)
    elif data["score"] < 8:
        median_dataset.append(data)

save_json(median_dataset, median)
save_json(hard_dataset, hard)