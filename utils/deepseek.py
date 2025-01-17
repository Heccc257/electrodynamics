
from openai import OpenAI
import json
import argparse
import os
from tqdm import tqdm

api_key = "sk-a81461b386a94a2cbe2c040f99cac1f3"

def save_json(data, output_path):

    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json_str)

def analyse_scope_of_knowledge(file_path):

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

        
    data = json.load(open(file_path, "r"))
    output_path = os.path.join("analysis", "sok_" + file_path.split('/')[-1]) # scope of knowlege
    analyses = []
    instruction = "你是一位电动力学领域的专家, 下面我会给出一个电动力学习题，请你分析一下这道题所用到的数理知识有哪些."

    print("begin to ask deepseek")
    print(f"file_path: {file_path}")
    print(f"output_path: {output_path}")
    f = open("analysis/analyse.txt", "w", encoding="utf-8")

    for idx, obj in enumerate(tqdm(data, desc="Processing questions")):
        question = obj["input"]
        analyse = {}
        analyse["instruction"] = instruction
        analyse["input"] = obj["input"]

        f.write(f"question {question}\n")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是一位电动力学领域的专家, 下面我会给出一个电动力学习题，请你分析一下这道题所用到的数理知识有哪些, 简短一些, 尽量不要超过2048个token"},
                {"role": "user", "content": f"{obj["input"]}"},
            ],
            stream=False
        )

        f.write(f"response: {response.choices[0].message.content}\n")
        f.flush()
        analyse["output"] = response.choices[0].message.content

        analyses.append(analyse)

        if idx%5 == 0:
            save_json(analyses, output_path)
        

    save_json(analyses, output_path)

def analyse_step_by_step(file_path):

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

        
    data = json.load(open(file_path, "r"))
    output_path = os.path.join("analysis", "sbs_" + file_path.split('/')[-1]) # scope of knowlege
    analyses = []
    instruction = "你是一位电动力学领域的专家, 下面我会给出一个电动力学习题以及答案, 请你帮我讲解一下思路,只需要说明每一步是如何想到的,与之前步骤以及题目的关联，如果之间有比较复杂的计算证明，请尽量详细的给出计算步骤."

    print("begin to ask deepseek")
    print(f"file_path: {file_path}")
    print(f"output_path: {output_path}")
    f = open("analysis/analyse.txt", "w", encoding="utf-8")

    for idx, obj in enumerate(tqdm(data, desc="Processing questions")):
        question = obj["input"]
        analyse = {}
        analyse["instruction"] = instruction
        analyse["input"] = f"question: {obj["input"]}\n\n answer: {obj["output"]}"

        f.write(f"question {question}\n")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": f"{instruction} \n 尽量简短一些, 4096个token"},
                {"role": "user", "content": f"{analyse["input"]}"},
            ],
            stream=False
        )

        f.write(f"response: {response.choices[0].message.content}\n")
        f.flush()
        analyse["output"] = response.choices[0].message.content

        analyses.append(analyse)

        if idx%5 == 0:
            save_json(analyses, output_path)
        

    save_json(analyses, output_path)

def expand_dataset(file_path):
    prompt = r"""我会给你一个电动力学的概念，请你为我出2-4道高质量的题应用这个概念。如果涉及公式需要有公式的应用或者推导，使用类似的json格式返回给我，一步一步思考
要严格遵循返回格式，保证返回的内容可以解析为json，并且不要返回代码块的形式，只需要返回json内容即可。例如：
[
  {
        "instruction": "problem1 description",
        "input": "",
        "output": "$\\epsilon_{ijk}$..."
  },
  {
        "instruction": "problem2 description",
        "input": "",
        "output": "$\\pmb{B}$ ..."
  },
  {
        "instruction": "problem3",
        "input": "",
        "output": "anser3"
  }
]
注意不要输出过多的\，例如换行符\\\\\n。但是注意公式要使用\\，例如\\sum，否则无法用python解析。
注意公式要使用$$，参考给你的电动力学概念

下面是给你的概念：
    """

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    datas = json.load(open(file_path, 'r'))

    expand_questions = []
    output_path = "./datasets/expand.json"
    wastes = open("./datasets/wastes.txt", "w")

    for idx, obj in enumerate(tqdm(datas, desc="Processing questions")):
        question = prompt + str(obj)
        expand_questions.append(obj)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "you are a helpful assistant"},
                {"role": "user", "content": question},
            ],
            stream=False
        )
        response = response.choices[0].message.content
        try:
            response = json.loads(response)
        except Exception as e:
            # 捕获其他可能的异常
            print(f"发生错误: {e}")
            print(str(response))
            wastes.write(str(response))
            continue
        expand_questions += response

        if idx%5 == 0 or idx < 5:
            save_json(expand_questions, output_path)
    
    save_json(expand_questions, output_path)

def reverse_textbook(file_path):
    prompt = r"""我会给你一个电动力学的概念，请你为我出5-10道高质量的题理解这个概念，题目是根据一段描述或者问题，分析出其中涉及到的电动力学知识或者技巧。如果涉及公式需要有公式的应用或者推导，一步一步思考。
    使用类似的json格式返回给我，要严格遵循返回格式，保证返回的内容可以使用python解析为json，只需要返回json内容即可。例如：

[
  {
        "instruction": "以下题目或者描述涉及的电动力学知识或者技巧",
        "input": "对于一个连续系统如场，诺特定理本质与离散系统相同，只是在部分数学计算上稍微麻烦一点，且物理量的守恒性由连续性方程表达。当我们考虑场时，时空坐标 $(x^{\\mu})$ 为自变量，而...",
        "output": "场的诺特定理; 代数运算... "
  },
  {
        "instruction": "以下题目或者描述涉及的电动力学知识或者技巧",
        "input": "题目2",
        "output": "知识点2..."
  }
]
并且不要返回代码块的形式 错误的例子：
```json
    xxxx
```

注意不要输出过多的\，例如换行符\\\\\n。但是注意公式要使用\\，例如\\sum，否则无法用python解析。
注意公式要使用$$，参考给你的电动力学概念

下面给出你需要参考的电动力学内容，要结合其中的内容出题
    """

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    datas = json.load(open(file_path, 'r'))

    expand_questions = []
    output_path = "./datasets/reverse.json"

    
    for idx, obj in enumerate(tqdm(datas, desc="Processing questions")):
        question = prompt + str(obj)
        if idx < 1:
            print(question)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "you are a helpful assistant"},
                {"role": "user", "content": question},
            ],
            stream=False
        )
        response = response.choices[0].message.content
        try:
            response = json.loads(response)
        except Exception as e:
            # 捕获其他可能的异常
            print(f"发生错误: {e}")
            print(str(response))
            
            continue
        expand_questions += response

        if idx%5 == 0 or idx < 5:
            save_json(expand_questions, output_path)
    
    save_json(expand_questions, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a JSON file with electrodynamics problems.")
    parser.add_argument("--file", type=str, help="Path to the JSON file containing the electrodynamics problems.")
    parser.add_argument("--analy", type=str)


    # 解析命令行参数
    args = parser.parse_args()
    analy = args.analy
    if analy == "sok": # scope of knowledge
        print("analyse scope of knowlege")
        analyse_scope_of_knowledge(args.file)
    elif analy == "sbs": # step by step
        print("analyse step by step")
        analyse_step_by_step(args.file)
    elif analy == "expand":
        print("expand")
        expand_dataset(args.file)
    elif analy == "textbook":
        print("textbook")
        reverse_textbook(args.file)
    else:
        print("unknown analayse")
        
