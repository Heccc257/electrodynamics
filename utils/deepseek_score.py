
from openai import OpenAI
import json
import argparse
import os
from tqdm import tqdm
import copy
import random
import time
import threading
import silicon_flow
import aliyun
# api_key = "sk-a81461b386a94a2cbe2c040f99cac1f3"
api_key = "sk-8d0ba939547b4585acd59da8a383efe0"
api_key = "sk-3ad9b85645f246788fc2f3ae474bc6a0"
# api_key = "sk-ceajxtcicytniffxkfcwfsqgyokeqnyxdctctrkongnnogxl"

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
        f.write(json_str)

def score(file_path):
    prompt = r"""
    下面将给出一个或者若干个电动力学问题以及对应的标准答案和回答，请为每道题的回答打分，分数从1-10。
    只需要输出分数即可，用json的格式返回，并且开头和结尾不需要返回```，只需要直接返回内容。
    参考下面的例子,返回的是一个json列表，列表中的每个元素只有两个键值"score"和"comment"。

    例子：```
    输入：
    [
        {
            "instruction": "描述麦克斯韦方程组在真空中的形式。",
            "standard": "\\begin{aligned} \\nabla \\cdot \\pmb{{\\cal E}} &= ...",
            "output": " ```json\n好，用户给了我一个问题：“描述麦克斯韦方程组在真空中的形式。”然后..."
        },
        {
            "instruction": "推导静电场中库仑定律的矢量形式。",
            "standard": "\\pmb{{\\cal E}} = \\frac{1}{4\\pi\\varepsilon_0} ...",
            "output": "\n\n\n</think>\n\n$$ \\mathbf{F}_{12} = ..."
        }
    ]
    输出：
    [
        {
            "score": 7,
            "comment": "..."
        },
        {
            "score": 8,
            "comment": "..."
        }
    ]

    ```
    
    下面将给出正式的问题和对应的回答：\n
    """
    # 注意思维链的公式要使用$$，并且在关键词前使用\\，例如\\sum,\\delta等，否则无法用python解析。
    # 例子：根据爱因斯坦求和约定，二阶张量 $T_{ij}$ 的迹 $\\text{Tr}(T)$ 可以表示为 $\\text{Tr}(T) = T_{ii}$，其中 $i$ 是哑指标，默认求和。\n单位张量 $\\delta_{ij}$ 的定义是 $\\delta_{ij} = 1$ 当 $i = j$。
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    datasets = json.load(open(file_path, 'r'))
    outputs = []
    output_path = "./datasets/score.json"

    with open(output_path, "w") as f:
        pass
    
    batch_size = 10

    datasets = [{"instruction": data["instruction"], "standard": data["standard"], "output": data["output"]} for data in datasets]

    random.shuffle(datasets)
    datasets = datasets[::5]

    data_batches = [datasets[i: min(i+batch_size, len(datasets))] for i in range(0, len(datasets), batch_size)]

    for idx, objs in enumerate(tqdm(data_batches, desc="Processing questions")):
        questions = json.dumps(objs, ensure_ascii=False, indent=4)


        messages = [{"role": "user", "content": f"{prompt + questions}"}]
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            # model="deepseek-chat",
            messages=messages
        )
        # reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content

        try:
            if idx < 2:
                print(f"sample response: {content}")
            answers = json.loads(content)
            opts = copy.deepcopy(objs)
            for i in range(batch_size):
                opts[i]["score"] = answers[i]["score"]
                opts[i]["comment"] = answers[i]["comment"]
            outputs += opts
            if len(outputs)%(batch_size*2) == 0:
                save_json(outputs, output_path)

        except Exception as e:
            # 捕获其他可能的异常
            print(f"发生错误: {e}")
            print(str(content))
            with open("./datasets/score_wastes.txt", "a") as wastes:
                wastes.write(str(content))
            continue


    save_json(outputs, output_path)

def median(file_path):
    prompt = r"""
    下面将给出一个或者若干个电动力学问题,对应的标准答案,回答以及打分和评论。
    根据回答的打分和评论，重新设计回答，使得回答更加符合要求，以便于我能更好的学习如何解决这个问题,如果认为有必要，还要需要补充若干(1-5道)相关的题目，同样的给出题目和回答,不需要包含"补充题目"等字样。
    要求你的回答给出比较复杂并且足够清晰的思考过程，思考过程用</think>包裹；回答用</answer>包裹.格式参考给你的例子。
    
    用json的格式返回，并且开头和结尾不需要返回```，只需要直接返回内容。
    参考下面的例子,返回的是一个json列表,注意你的列表中的每个元素只有两个键值"input"和"output"，要严格按照给你的例子输出

    例子：```
    User:
    [
        {
            "instruction": "Lorentz力密度是如何表示的？",
            "standard": "...",
            "score": 7,
            "comment": "回答基本正确，但推导过程较为冗长，且部分表述不够简洁，与标准答案的简洁性有一定差距。"
        },
        {
            "instruction": "Biot-Savart 定律描述了___。",
            "standard": "...",
            "output": " ...",
            "score": 6,
            "comment": "回答虽然提到了Biot-Savart定律的数学表达式和应用，但开头部分的内容与问题无关，且没有直接回答Biot-Savart定律描述的内容。"
        }
    ]
    Assistant:
    [
        {
            "input": "题目描述1",
            "output": "<think></think> <answer></answer>"
        },
        {
            "input": "题目描述2",
            "output": "<think></think> <answer></answer>"
        }
    ]
    ```
    
    下面将给出正式的数据：\n
    """
    # 注意思维链的公式要使用$$，并且在关键词前使用\\，例如\\sum,\\delta等，否则无法用python解析。
    # 例子：根据爱因斯坦求和约定，二阶张量 $T_{ij}$ 的迹 $\\text{Tr}(T)$ 可以表示为 $\\text{Tr}(T) = T_{ii}$，其中 $i$ 是哑指标，默认求和。\n单位张量 $\\delta_{ij}$ 的定义是 $\\delta_{ij} = 1$ 当 $i = j$。
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    datasets = json.load(open(file_path, 'r'))
    outputs = []
    output_path = "./datasets/median_sup.json"

    with open(output_path, "w") as f:
        pass
    
    batch_size = 3

    data_batches = [datasets[i: min(i+batch_size, len(datasets))] for i in range(0, len(datasets), batch_size)]

    lock = threading.Lock()
    def process_batch(idx, objs):
        nonlocal outputs
        nonlocal lock
        
        questions = json.dumps(objs, ensure_ascii=False, indent=4)

        # if idx < 2:
        #     print(f"sample question: {questions}")

        messages = [{"role": "user", "content": f"{prompt + questions}"}]
        response = client.chat.completions.create(
            # model="deepseek-reasoner",
            model="deepseek-chat",
            messages=messages
        )
        # reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content
        # print("content")
        with lock:
            try:
                # if idx < 2:
                #     print(f"sample response: {content}")
                answers = json.loads(content)
                outputs += answers
                save_json(outputs, output_path)

            except Exception as e:
                # 捕获其他可能的异常
                print(f"发生错误: {e}")
                print(str(content))
                with open("./datasets/median_wastes.txt", "a") as wastes:
                    wastes.write(str(content))

    threads = []
    for idx, objs in enumerate(tqdm(data_batches, desc="Processing questions")):
        
        t = threading.Thread(target=process_batch, args=(idx, objs))
        t.start()
        threads.append(t)
        questions = json.dumps(objs, ensure_ascii=False, indent=4)
        if idx%10 == 0:
            for t in threads:
                t.join()
        # if idx < 2:
        #     print(f"sample question: {questions}")

        # messages = [{"role": "user", "content": f"{prompt + questions}"}]
        # response = client.chat.completions.create(
        #     # model="deepseek-reasoner",
        #     model="deepseek-chat",
        #     messages=messages
        # )
        # # reasoning_content = response.choices[0].message.reasoning_content
        # content = response.choices[0].message.content
        # # print("content")
        # try:
        #     # if idx < 2:
        #     #     print(f"sample response: {content}")
        #     answers = json.loads(content)
        #     outputs += answers
        #     if idx%2 == 0:
        #         save_json(outputs, output_path)

        # except Exception as e:
        #     # 捕获其他可能的异常
        #     print(f"发生错误: {e}")
        #     print(str(content))
        #     with open("./datasets/median_wastes.txt", "a") as wastes:
        #         wastes.write(str(content))
        #     continue


    save_json(outputs, output_path)

def hard(file_path):
    # 你需要将你自己的思考过程和自我反思过程整理好一并放到输出当中，不要太短,要全面，思考过程用<think></think>包裹，答案用<answer></answer>包裹。要求思考过程要详细。
    prompt = r"""
    我将给出一个电动力学问题，同时可能给出参考答案，一步一步思考并解决这个问题。
    注意公式使用latex格式，使用$$包裹。
    下面将给出正式的问题：\n
    """
    # 注意思维链的公式要使用$$，并且在关键词前使用\\，例如\\sum,\\delta等，否则无法用python解析。
    # 例子：根据爱因斯坦求和约定，二阶张量 $T_{ij}$ 的迹 $\\text{Tr}(T)$ 可以表示为 $\\text{Tr}(T) = T_{ii}$，其中 $i$ 是哑指标，默认求和。\n单位张量 $\\delta_{ij}$ 的定义是 $\\delta_{ij} = 1$ 当 $i = j$。

    # client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    client = OpenAI(api_key="sk-90db01b7652f459bb3295de1aac85967", base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")


    datasets = json.load(open(file_path, 'r'))
    outputs = []
    output_path = "./datasets/hard_sup.json"
    lock = threading.Lock()

    with open(output_path, "w") as f:
        pass
    with open("./datasets/hard_wastes.txt", "w") as f:
        pass
    
    batch_size = 1
    datasets = [{"input": data["input"], "output": data["output"] if "output" in data.keys() else ""} for data in datasets]

    data_batches = [datasets[i: min(i+batch_size, len(datasets))] for i in range(0, len(datasets), batch_size)]

    def process_batch(idx, objs):
        nonlocal outputs
        nonlocal lock

        questions = json.dumps(objs, ensure_ascii=False, indent=4)

        # messages = [{"role": "user", "content": f"{prompt + questions}"}]
        # response = client.chat.completions.create(
        #     # model="deepseek-reasoner",
        #     # model="deepseek-chat",
        #     model="deepseek-v3", 
        #     messages=messages,
        #     temperature=0.1
        # )
        # # reasoning_content = response.choices[0].message.reasoning_content
        # content = response.choices[0].message.content
        # reasoning_content = response.choices[0].message.reasoning_content
        # print(content)

        # content = content.replace("<think>", "").replace("</think>", "").replace("<answer>", "").replace("</answer>", "")
        # reasoning_content = reasoning_content.replace("<think>", "").replace("</think>", "").replace("<answer>", "").replace("</answer>", "")
        
        prompt = r"""我将给出一个电动力学问题，同时可能给出参考答案，一步一步思考并解决这个问题。思考过程用<think></think>包裹，答案用<answer></answer>包裹。
        注意公式使用latex格式，使用$$包裹。
        下面将给出正式的问题和参考资料：\n
        """
        questions = f"{prompt + questions}"
        if idx == 0:
            print(f"sample question: {questions}")
        content = aliyun.ask_aliyun(questions)

        with lock:
            try:
                answers = {}
                answers["input"] = objs[0]["input"]
                # answers["output"] = f"<think>{reasoning_content}</think>\n<answer>{content}</answer>"
                answers["output"] = content

                outputs.append(answers)
                save_json(outputs, output_path)


            except Exception as e:
                # 捕获其他可能的异常
                print(f"发生错误: {e}")
                # print(str(reasoning_content))
                print(str(content))
                with open("./datasets/hard_wastes.txt", "a") as wastes:
                    wastes.write(str(idx) + "\n")
                    wastes.write(str(content) + "\n\n")

    threads = []
    for idx, objs in enumerate(tqdm(data_batches, desc="Processing questions")):
        t = threading.Thread(target=process_batch, args=(idx, objs))
        t.start()
        threads.append(t)

        if idx%8 == 0:
            for t in threads:
                t.join()

    save_json(outputs, output_path)

def choose(file_path):
    # 你需要将你自己的思考过程和自我反思过程整理好一并放到输出当中，不要太短,要全面，思考过程用<think></think>包裹，答案用<answer></answer>包裹。要求思考过程要详细。
    prompt = r"""
    我将给出一个电动力学问题，同时可能给出参考答案，一步一步思考并解决这个问题。
    注意公式使用latex格式，使用$$包裹。
    下面将给出正式的问题：\n
    """
    # 注意思维链的公式要使用$$，并且在关键词前使用\\，例如\\sum,\\delta等，否则无法用python解析。
    # 例子：根据爱因斯坦求和约定，二阶张量 $T_{ij}$ 的迹 $\\text{Tr}(T)$ 可以表示为 $\\text{Tr}(T) = T_{ii}$，其中 $i$ 是哑指标，默认求和。\n单位张量 $\\delta_{ij}$ 的定义是 $\\delta_{ij} = 1$ 当 $i = j$。

    # client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    client = OpenAI(api_key="sk-90db01b7652f459bb3295de1aac85967", base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")


    datasets = json.load(open(file_path, 'r'))
    outputs = []
    output_path = "./datasets/choose.json"
    lock = threading.Lock()

    with open(output_path, "w") as f:
        pass
    with open("./datasets/choose_wastes.txt", "w") as f:
        pass
    
    batch_size = 1
    datasets = [{"instruction": data["instruction"], "output": data["output"] if "output" in data.keys() else ""} for data in datasets]

    data_batches = [datasets[i: min(i+batch_size, len(datasets))] for i in range(0, len(datasets), batch_size)]

    def process_batch(idx, objs):
        nonlocal outputs
        nonlocal lock

        questions = json.dumps(objs, ensure_ascii=False, indent=4)
        obj = objs[0]
        # messages = [{"role": "user", "content": f"{prompt + questions}"}]
        # response = client.chat.completions.create(
        #     # model="deepseek-reasoner",
        #     # model="deepseek-chat",
        #     model="deepseek-v3", 
        #     messages=messages,
        #     temperature=0.1
        # )
        # # reasoning_content = response.choices[0].message.reasoning_content
        # content = response.choices[0].message.content
        # reasoning_content = response.choices[0].message.reasoning_content
        # print(content)

        # content = content.replace("<think>", "").replace("</think>", "").replace("<answer>", "").replace("</answer>", "")
        # reasoning_content = reasoning_content.replace("<think>", "").replace("</think>", "").replace("<answer>", "").replace("</answer>", "")
        
        prompt = r"""我将给出一个电动力学问题，以及若干个回答，从0开始编号。
        根据答案正确性和思维完整性选择最好的一个，只需要输出编号。

        """
        questions = f"{prompt + questions}"
        if idx == 0:
            print(f"sample question: {questions}")
        content = aliyun.ask_aliyun(questions)
        best = 0
        for i in range(len(obj["output"])):
            if str(i) in content:
                best = i
                break
        
        with lock:
            try:
                for i in range(len(obj["output"])):
                    if i == best: continue
                    answers = {}
                    answers["instruction"] = "下面将给出一个电动力学问题，请一步一步思考，使用中文给出思考过程和解答。\n    要求思考过程详细，解答要尽量简洁,思考过程用<think></think>包裹,解答用<answer></answer>包裹\n    注意公式使用$$\n    例如：```\n    User: \"在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式是如何与加速度的平行和垂直分量相关的？\"\n    Assistant: \"<think>在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式可以通过粒子的加速度 $\\boldsymbol{a}$ 的平行和垂直分量来描述。...</think>\\n <answer>线性加速器中，粒子的速度 $\\mathbf{v}$ 与加速度 ...</answer>\"\n    ```\n    下面是问题：\n\n" + obj["instruction"]
                    answers["chosen"] = obj["output"][best]
                    answers["rejected"] = obj["output"][i]
                    # answers["content"] = content
                    outputs.append(answers)

            except Exception as e:
                # 捕获其他可能的异常
                print(f"发生错误: {e}")
                # print(str(reasoning_content))
                print(str(content))
                with open("./datasets/hard_wastes.txt", "a") as wastes:
                    wastes.write(str(idx) + "\n")
                    wastes.write(str(content) + "\n\n")

    threads = []
    for idx, objs in enumerate(tqdm(data_batches, desc="Processing questions")):
        t = threading.Thread(target=process_batch, args=(idx, objs))
        t.start()
        threads.append(t)

        if idx%8 == 0:
            for t in threads:
                t.join()

            save_json(outputs, output_path)

    save_json(outputs, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a JSON file with electrodynamics problems.")
    parser.add_argument("--file", type=str, help="Path to the JSON file containing the electrodynamics problems.")
    parser.add_argument("--analy", type=str)


    # 解析命令行参数
    args = parser.parse_args()
    analy = args.analy
    if analy == "score": # scope of knowledge
        print("score")
        score(args.file)
    elif analy == "median":
        print("median")
        median(args.file)
    elif analy == "hard":
        print("hard")
        hard(args.file)
    elif analy == "choose":
        print("choose")
        choose(args.file)
    else:
        print("unknown analayse")
        
