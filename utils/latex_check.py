from openai import OpenAI
import json
import argparse
import os
from tqdm import tqdm
import copy
import time
import threading
import io
from contextlib import redirect_stdout

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
        f.write(json_str)

def check_latex(file_path):
    latex_prompt = """
    我会给你一段内容，检查其中latex公式有没有格式错误，如果没有直接原文返回给我，不要输出多余内容，否则修正后全部返回给我
    公式不要使用\\(\\)，而是使用$$
    公式内不要有多余的转义符号，例如将$\\\\frac$改成$\\frac$,将$\\\\boldsymbol{A}$改成$\\boldsymbol{A}$。

    User: 
        给定一个二阶张量 \\(T_{ij}\\)
        $\\\\epsilon$
    Assitant: 
        给定一个二阶张量 $(T_{ij}$
        $\\epsilon$

    下面是内容：\n
        
    """
    client = OpenAI(
        api_key = "fb37da60-b6f8-4f33-a955-7b0e96c4af64",
        base_url = "https://ark.cn-beijing.volces.com/api/v3",
    )
    lock = threading.Lock()

    outputs = []
    output_path = "./datasets/latex.json"

    with open(output_path, "w") as f:
        pass
    
    thread_size = 2
    batch_size = 10 * thread_size
    
    datasets = json.load(open(file_path, 'r'))
    data_batches = [datasets[i: min(i+batch_size, len(datasets))] for i in range(0, len(datasets), batch_size)]

    def process_batch(idx, objs):
        nonlocal outputs
        nonlocal lock
        
        questions = latex_prompt + str(json.dumps(objs, ensure_ascii=False, indent=4))
    
        
        questions = questions.replace(r"\\", "\\").replace(r"\n", "@")
        # print(questions)
        messages = [{"role": "user", "content": f"{questions}"}]


        completion = client.chat.completions.create(
            model = "ep-20250124143019-2dn6m", # your model endpoint ID
            messages=messages,
            temperature=0.0
        )
        content = completion.choices[0].message.content

        content = content.replace("\\", "\\\\").replace("@", r"\n")

        with lock:

            try:
                opts = json.loads(content)

                outputs += opts
                if idx < 5 or idx%5 == 0:
                    save_json(outputs, output_path)
            except Exception as e:
                # 捕获其他可能的异常
                print(f"发生错误: {e}")
                # print(content)
                with open("./datasets/latex_wastes.txt", "a") as wastes:
                    wastes.write(content + "\n")
    for idx, objs in enumerate(tqdm(data_batches, desc="Processing questions")):
        # process_batch(idx, objs[0: thread_size])
        # exit(0)
        threads = []
        for i in range(0, batch_size, thread_size):
            threads.append(threading.Thread(target=process_batch, args=(idx, objs[i: i+thread_size])))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, default="./datasets/latex.json")
    args = parser.parse_args()
    check_latex(args.file)