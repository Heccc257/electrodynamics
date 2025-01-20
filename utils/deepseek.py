
from openai import OpenAI
import json
import argparse
import os
from tqdm import tqdm

api_key = "sk-a81461b386a94a2cbe2c040f99cac1f3"

def save_json(data, output_path, append=False):
    open_type = "w"
    if append == True:
        open_type = "a"
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    with open(output_path, open_type, encoding="utf-8") as f:
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

    for idx, obj in enumerate(tqdm(datas, desc="Processing questions")):

        # temporary 
        if idx < 565:
            continue



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
            with open("./datasets/expand_wastes.txt", "a") as wastes:
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

def check_latex_format(client, response):
    latex_prompt = r"""我会给你一段内容，检查其中latex公式有没有格式错误，如果没有直接原文返回给我，不要输出多余内容，否则修正后全部返回给我
    要求对于\sum \frac 等公式，特殊符号，需要使用\\将\转义为纯文本
    例如：
        输入：
        [
            {
                "instruction": "在电动力学中，$P_{l}(\cos\theta)$ 表示___。",
                "input": "",
                "output": "勒让德多项式"
            },
            {
                "instruction": "使用爱因斯坦求和约定，向量 $\pmb{A}=A_{1}\pmb{e}_{1}+A_{2}\pmb{e}_{2}+A_{3}\pmb{e}_{3}$ 可以表达为___。",
                "input": "",
                "output": "$A_{i}{e_{i}}$"
            }
        ]
        输出：
        [
            {
                "instruction": "在电动力学中，$P_{l}(\\cos\\theta)$ 表示___。",
                "input": "",
                "output": "勒让德多项式"
            },
            {
                "instruction": "使用爱因斯坦求和约定，向量 $\\pmb{A}=A_{1}\\pmb{e}_{1}+A_{2}\\pmb{e}_{2}+A_{3}\\pmb{e}_{3}$ 可以表达为___。",
                "input": "",
                "output": "$A_{i}{e_{i}}$"
            }
        ]

    下面是要给你的内容\n
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "you are a helpful assistant"},
            {"role": "user", "content": latex_prompt + response},
        ],
        stream=False
    )
    response = response.choices[0].message.content

    return response

def blank_textbook(file_path):
    prompt = r"""我会给你一个电动力学的概念，请你根据内容的质和量出3-6道高质量的基础知识问答来帮我更好地理解和记忆这些内容,重点在于理解和学习电动力学概念.（内容太多的情况下要多出几道题,不需要出过多的重复的题）。
    你要分析给你的电动力学内容，最好截取有价值的原文片段，！！！
    如果你引用了原文的内容或者题目，需要将引用的内容也一并包含在题干中，不需要写出文中的题号，例如：
        例题1.4中xxx:  
        (用下标法证明 $\\nabla\\cdot\\left(\\mathbf{A}\\times B\\right)=B\\cdot\\nabla\\times A-A\\cdot\\nabla\\times ......)
    你出的题，不要出单纯的计算题，可以截取例题。
    使用类似的json格式返回给我，要严格遵循返回格式，保证返回的内容可以使用python解析为json，只需要返回json内容即可。例如：
        输入：三维狄拉克函数的定义为  \n\n$$\n\\delta(\\pmb{r})=\\delta(x)\\delta(y)\\delta(z),\n$$  \n\n这里 $\\pmb{r}=x\\pmb{e}_{x}+y\\pmb{e}_{y}+z\\pmb{e}_{z}$ 是位移矢量
        返回：
        [
            {
                "instruction": "三维狄拉克函数的定义为",
                "input": "",
                "output": "$$\n\\delta(\\pmb{r})=\\delta(x)\\delta(y)\\delta(z),\n$$ "
            },
            {
                "instruction": "xxx",
                "input": "",
                "output": "xxxx"
            }
        ]
    并且不要返回代码块的形式 错误的例子：
    ```json
        xxxx
    ```

    注意不要输出过多的\，例如换行符\\\\\n。但是注意公式要使用\\，例如\\sum,\\delta等，否则无法用python解析。
    注意公式要使用$$，参考给你的电动力学概念。尽量与原文高度相关

    下面给出你需要参考的电动力学内容，要结合其中的内容出题：
    """

    latex_prompt = r"""我会给你一段内容，检查其中latex公式有没有格式错误，如果没有直接原文返回给我，不要输出多余内容，否则修正后全部返回给我
    要求对于\sum \frac 等公式，特殊符号，需要使用\\将\转义为纯文本
    例如：
        输入：
        [
            {
                "instruction": "在电动力学中，$P_{l}(\cos\theta)$ 表示___。",
                "input": "",
                "output": "勒让德多项式"
            },
            {
                "instruction": "使用爱因斯坦求和约定，向量 $\pmb{A}=A_{1}\pmb{e}_{1}+A_{2}\pmb{e}_{2}+A_{3}\pmb{e}_{3}$ 可以表达为___。",
                "input": "",
                "output": "$A_{i}{e_{i}}$"
            }
        ]
        输出：
        [
            {
                "instruction": "在电动力学中，$P_{l}(\\cos\\theta)$ 表示___。",
                "input": "",
                "output": "勒让德多项式"
            },
            {
                "instruction": "使用爱因斯坦求和约定，向量 $\\pmb{A}=A_{1}\\pmb{e}_{1}+A_{2}\\pmb{e}_{2}+A_{3}\\pmb{e}_{3}$ 可以表达为___。",
                "input": "",
                "output": "$A_{i}{e_{i}}$"
            }
        ]

    下面是要给你的内容\n
    """

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    datas = json.load(open(file_path, 'r'))

    blank_questions = []
    output_path = "./datasets/blank.json"

    with open(output_path, "w") as f:
        pass
    
    for idx, obj in enumerate(tqdm(datas, desc="Processing questions")):
        content = obj["content"]
        
        setences = content.split('。')

        step = 3
        strip = 10

        # i-step+strip < len(sentences)
        # ranges = [0] + [i for i in range(step, len(setences)+step-strip, step)]
        ranges = [0] + [i for i in range(step, len(setences), step)]
        print(f"sentences num: {len(setences)}    ranges: {ranges}")
        for i in ranges:
            selected_content = ". ".join(setences[i: min(i+strip, len(setences))])
            selected_content = "title: " + obj["title"] + "\n" + selected_content

            question = prompt + selected_content
            if idx < 1 and i < 2 * step:
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

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "you are a helpful assistant"},
                    {"role": "user", "content": latex_prompt + response},
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
                with open("./datasets/blank_waste.txt", "a") as f:
                    f.write(str(response))
                continue
            blank_questions += response

            if idx%5 == 0 or idx < 5:
                save_json(blank_questions, output_path)
    
    save_json(blank_questions, output_path)

def origin_textbook(file_path):
    prompt = r"""下面我会给你一个电动力学的教材片段，帮我处理一下格式
    对于title部分，将其变为一个问句，并且不要出现如1.4等编号
    对于content部分，去掉其中没有关键作用的描述，只保留关键的论述和公式.
    用json的格式返回给我，格式如下，只需要返回json本体就行了，不需要开头和结尾的```标记
        [
            {
                "instruction": "在电动力学中，$P_{l}(\cos\theta)$ 表示___。",
                "input": "",
                "output": "勒让德多项式"
            },
            {
                "instruction": "使用爱因斯坦求和约定，向量 $\pmb{A}=A_{1}\pmb{e}_{1}+A_{2}\pmb{e}_{2}+A_{3}\pmb{e}_{3}$ 可以表达为___。",
                "input": "",
                "output": "$A_{i}{e_{i}}$"
            }
        ]
    
    """
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    datas = json.load(open(file_path, 'r'))

    origin_questions = []
    output_path = "./datasets/origin.json"

    with open(output_path, "w") as f:
        pass
    
    for idx, obj in enumerate(tqdm(datas, desc="Processing questions")):
        title = obj["title"]
        content = obj["content"]
        
        setences = content.split('。')
            
        question = prompt + f"title: {title} \n\n content: {content}"

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "you are a helpful assistant"},
                {"role": "user", "content": question},
            ],
            stream=False
        )
        response = response.choices[0].message.content

        response = check_latex_format(client, response)
        if idx < 1:
            print(f"response: {response}")

        try:
            response = json.loads(response)
        except Exception as e:
            # 捕获其他可能的异常
            print(f"发生错误: {e}")
            print(str(response))
            with open("./datasets/origin_waste.txt", "a") as f:
                f.write(str(response))
            continue

        origin_questions += response
        
        if idx%5 == 0 or idx < 5:
            save_json(origin_questions, output_path)
    
    save_json(origin_questions, output_path)


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
    elif analy == "reverse":
        print("reverse")
        reverse_textbook(args.file)
    elif analy == "blank":
        print("blank")
        blank_textbook(args.file)
    elif analy == "origin":
        print("origin")
        origin_textbook(args.file)
    else:
        print("unknown analayse")
        
