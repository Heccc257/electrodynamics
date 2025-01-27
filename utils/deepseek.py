
from openai import OpenAI
import json
import argparse
import os
from tqdm import tqdm
import copy
import time

# api_key = "sk-a81461b386a94a2cbe2c040f99cac1f3"
api_key = "sk-8d0ba939547b4585acd59da8a383efe0"

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

def reasoner(file_path):
    # prompt = r"""
    # 根据下列的电动力学的问题以及解答，给出思维过程，思维过程尽量简洁，不超过4096个token，每一个步骤用<|>隔开。
    # 例子：根据爱因斯坦求和约定，二阶张量 $T_{ij}$ 的迹 $\\text{Tr}(T)$ 可以表示为 $\\text{Tr}(T) = T_{ii}$，其中 $i$ 是哑指标，默认求和。\n单位张量 $\\delta_{ij}$ 的定义是 $\\delta_{ij} = 1$ 当 $i = j$。
    # 问题和解答如下：\n\n
    # """
    prompt = r"""
    下面将给出一个或者若干个电动力学问题(可能会包含对应的标准答案)，只需要分别返回每道题的思考过程，尽量地简洁，每个思考过程最好不要超过4096个token，每一个步骤用<|>隔开。
    注意公式使用$$并且关键字前使用\\,比如$\\sum_i$, $\\frac a b $ 
    注意输出格式，只需要返回对应的若干解答，用json的格式返回，并且开头和结尾不需要返回```，只需要直接返回内容。
    参考下面的例子,返回的是一个json列表，列表中的每个元素只有一个键值"cot"。
    例子：```
    输入：
    [
        {
            "instruction": "在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式是如何与加速度的平行和垂直分量相关的？",
            "output": "电场 $\\boldsymbol{E}$ 的表达式可以分解为 $$\\boldsymbol{E} = e_{R} \\times [(e_{R} - \\beta) \\times \\dot{\\beta}_{\\parallel}] + e_{R} \\times [(e_{R} - \\beta) \\times \\dot{\\beta}_{\\perp}],$$ 其中 $\\dot{\\beta}_{\\parallel}$ 和 $\\dot{\\beta}_{\\perp}$ 分别是加速度的平行和垂直分量。"
        },
        {
            "instruction": "在相对论粒子的辐射中，交叉项 $\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}}$ 的表达式是什么？",
            "output": "交叉项 $\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}}$ 的表达式为 $$\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}} \\propto 2\\{e_{R} \\times [(e_{R} - \\beta) \\times \\dot{\\beta}_{\\parallel}]\\} \\cdot \\{e_{R} \\times [(e_{R} - \\beta) \\times \\dot{\\beta}_{\\perp}]\\}.$$"
        }
    ]

    输出：
    [
        {
            "cot": "<|>在相对论粒子的辐射中，电场 $\\\\boldsymbol{E}$ 的表达式可以通过粒子的加速度 $\\\\boldsymbol{a}$ 的平行和垂直分量来描述。<|>首先，粒子的加速度 $\\\\boldsymbol{a}$ 可以分解为平行于速度 $\\\\boldsymbol{v}$ 的分量 $\\\\boldsymbol{a}_\\\\parallel$ 和垂直于速度 $\\\\boldsymbol{v}$ 的分量 $\\\\boldsymbol{a}_\\\\perp$。<|>根据相对论电动力学，电场 $\\\\boldsymbol{E}$ 的表达式为：\n$$\n\\\\boldsymbol{E} = \\\\frac{q}{4\\\\pi\\\\epsilon_0} \\\\left( \\\\frac{\\\\boldsymbol{n} - \\\\boldsymbol{\\\\beta}}{\\\\gamma^2 (1 - \\\\boldsymbol{\\\\beta} \\\\cdot \\\\boldsymbol{n})^3 R^2} + \\\\frac{\\\\boldsymbol{n} \\\\times [(\\\\boldsymbol{n} - \\\\boldsymbol{\\\\beta}) \\\\times \\\\boldsymbol{a}]}{c^2 (1 - \\\\boldsymbol{\\\\beta} \\\\cdot \\\\boldsymbol{n})^3 R} \\\\right)\n$$\n其中 $\\\\boldsymbol{\\\\beta} = \\\\boldsymbol{v}/c$，$\\\\gamma = 1/\\\\sqrt{1 - \\\\beta^2}$，$\\\\boldsymbol{n}$ 是观测方向的单位矢量，$R$ 是粒子到观测点的距离。<|>电场 $\\\\boldsymbol{E}$ 的辐射部分主要与加速度的垂直分量 $\\\\boldsymbol{a}_\\\\perp$ 相关，因为 $\\\\boldsymbol{a}_\\\\perp$ 会产生辐射场，而平行分量 $\\\\boldsymbol{a}_\\\\parallel$ 对辐射场的贡献较小。<|>因此，电场 $\\\\boldsymbol{E}$ 的辐射部分可以近似表示为：\n$$\n\\\\boldsymbol{E} \\\\approx \\\\frac{q}{4\\\\pi\\\\epsilon_0} \\\\frac{\\\\boldsymbol{n} \\\\times (\\\\boldsymbol{n} \\\\times \\\\boldsymbol{a}_\\\\perp)}{c^2 (1 - \\\\boldsymbol{\\\\beta} \\\\cdot \\\\boldsymbol{n})^3 R}\n$$\n这表明电场 $\\\\boldsymbol{E}$ 的辐射部分主要由加速度的垂直分量 $\\\\boldsymbol{a}_\\\\perp$ 决定。"
        },
        {
            "cot": "<|>首先，考虑相对论粒子的辐射功率分布。辐射功率的角分布通常由两部分组成：平行极化分量和垂直极化分量。交叉项 $\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}}$ 表示这两个极化分量之间的干涉项。<|>根据电动力学理论，辐射功率的角分布可以表示为：\n$$\n\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega} = \\frac{e^2}{4\\pi c} \\left| \\int_{-\\infty}^{\\infty} \\frac{\\mathbf{n} \\times [(\\mathbf{n} - \\boldsymbol{\\beta}) \\times \\dot{\\boldsymbol{\\beta}}]}{(1 - \\mathbf{n} \\cdot \\boldsymbol{\\beta})^3} e^{i\\omega(t - \\mathbf{n} \\cdot \\mathbf{r}(t)/c)} \\mathrm{d}t \\right|^2\n$$\n其中，$\\mathbf{n}$ 是观测方向的单位矢量，$\\boldsymbol{\\beta} = \\mathbf{v}/c$ 是粒子的速度矢量，$\\dot{\\boldsymbol{\\beta}}$ 是加速度矢量。<|>交叉项 $\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}}$ 可以通过将平行和垂直极化分量的辐射场进行干涉得到。具体表达式为：\n$$\n\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}} = \\frac{e^2}{4\\pi c} \\Re \\left[ \\left( \\int_{-\\infty}^{\\infty} \\frac{\\mathbf{n} \\times [(\\mathbf{n} - \\boldsymbol{\\beta}) \\times \\dot{\\boldsymbol{\\beta}}]_{\\parallel}}{(1 - \\mathbf{n} \\cdot \\boldsymbol{\\beta})^3} e^{i\\omega(t - \\mathbf{n} \\cdot \\mathbf{r}(t)/c)} \\mathrm{d}t \\right) \\cdot \\left( \\int_{-\\infty}^{\\infty} \\frac{\\mathbf{n} \\times [(\\mathbf{n} - \\boldsymbol{\\beta}) \\times \\dot{\\boldsymbol{\\beta}}]_{\\perp}}{(1 - \\mathbf{n} \\cdot \\boldsymbol{\\beta})^3} e^{-i\\omega(t - \\mathbf{n} \\cdot \\mathbf{r}(t)/c)} \\mathrm{d}t \\right) \\right]\n$$\n其中，$\\Re$ 表示取实部，$\\parallel$ 和 $\\perp$ 分别表示平行和垂直极化分量。<|>"
        }
    ]

    下面将给出正式的问题：\n
    """
    # 注意思维链的公式要使用$$，并且在关键词前使用\\，例如\\sum,\\delta等，否则无法用python解析。
    # 例子：根据爱因斯坦求和约定，二阶张量 $T_{ij}$ 的迹 $\\text{Tr}(T)$ 可以表示为 $\\text{Tr}(T) = T_{ii}$，其中 $i$ 是哑指标，默认求和。\n单位张量 $\\delta_{ij}$ 的定义是 $\\delta_{ij} = 1$ 当 $i = j$。
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    datasets = json.load(open(file_path, 'r'))
    outputs = []
    output_path = "./datasets/reasoner.json"

    with open(output_path, "w") as f:
        pass

    batch_size = 5
    datasets = [{"instruction": data["instruction"], "output": data["output"]} for data in datasets]
    data_batches = [datasets[i: min(i+batch_size, len(datasets))] for i in range(0, len(datasets), batch_size)]


    for idx, obj in enumerate(tqdm(data_batches, desc="Processing questions")):
        questions = json.dumps(obj, ensure_ascii=False, indent=4)
        

        messages = [{"role": "user", "content": f"{prompt + questions}"}]

        if idx < 2:
            print(f"question example: {prompt + questions}")
            
        response = client.chat.completions.create(
            # model="deepseek-reasoner",
            model="deepseek-chat",
            messages=messages
        )
        # reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content

        try:
            answers = json.loads(content)
            opts = copy.deepcopy(obj)
            for idx in range(batch_size):
                opts[idx]["cot"] = answers[idx]["cot"]
            outputs += opts
            if idx < 5 or idx%5 == 0:
                save_json(outputs, output_path)

        except Exception as e:
            # 捕获其他可能的异常
            print(f"发生错误: {e}")
            with open("./datasets/reasoner_wastes.txt", "a") as wastes:
                wastes.write(str(content))
            continue

        if idx < 5 or idx%5 == 0:
            save_json(outputs, output_path)

    save_json(outputs, output_path)

def answer_cot(file_path):
    prompt = r"""
    下面将给出一个或者若干个电动力学问题以及对应的参考答案，请分别为每道题给出对应的解答。
    注意公式使用$$并且关键词前使用\\,比如$\\sum$, $\\frac a b $。保证我能用python的json.loads()函数解析。
    输出只需要返回json的格式，不需要其他的内容。
    格式参考下面的例子，返回一个json列表，必要包含```json等格式内容，每个元素对应一道题，只有两个键值"input"和"output"分别表示问题和答案，返回json的元素数量必须与输入的题目数量一致。
    你需要将你自己的思考过程和自我反思过程整理好一并放到输出当中，不要太短,要全面和详细，思考过程用<think></think>包裹，答案用<answer></answer>包裹。

    例子：```
    输入：
    [
        {
            "instruction": "在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式是如何与加速度的平行和垂直分量相关的？",
            "input": "",
            "output": "线性加速器对应 $\\boldsymbol{v}\\parallel\\dot{\\boldsymbol{v}}$ 的情况..."
        },
        {
            "instruction": "在相对论粒子的辐射中，交叉项 $\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}}$ 的表达式是什么？",
            "input": "",
            "output": "交叉项 $\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}}$ 的表达式为..."
        }
    ]

    输出：
    [
        {
            "input": "在相对论粒子的辐射中，电场 $\\boldsymbol{E}$ 的表达式是如何与加速度的平行和垂直分量相关的？",
            "output": "<think>...</think>\n<answer>...</answer>"
        },
        {
            "input": "在相对论粒子的辐射中，交叉项 $\\left(\\frac{\\mathrm{d}P}{\\mathrm{d}\\Omega}\\right)_{\\mathrm{cross}}$ 的表达式是什么？",
            "output": "<think>...</think>\n<answer>...</answer>"
        }
    ]

    ```
    
    下面将给出正式的问题和参考答案：\n
    """
    # 注意思维链的公式要使用$$，并且在关键词前使用\\，例如\\sum,\\delta等，否则无法用python解析。
    # 例子：根据爱因斯坦求和约定，二阶张量 $T_{ij}$ 的迹 $\\text{Tr}(T)$ 可以表示为 $\\text{Tr}(T) = T_{ii}$，其中 $i$ 是哑指标，默认求和。\n单位张量 $\\delta_{ij}$ 的定义是 $\\delta_{ij} = 1$ 当 $i = j$。
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    datasets = json.load(open(file_path, 'r'))
    outputs = []
    output_path = "./datasets/answer.json"

    with open(output_path, "w") as f:
        pass
    
    batch_size = 5
    datasets = [{"instruction": data["instruction"], "output": data["output"]} for data in datasets]

    data_batches = [datasets[i: min(i+batch_size, len(datasets))] for i in range(0, len(datasets), batch_size)]

    for idx, objs in enumerate(tqdm(data_batches, desc="Processing questions")):
        questions = json.dumps(objs, ensure_ascii=False, indent=4)


        messages = [{"role": "user", "content": f"{prompt + questions}"}]

        if idx < 2:
            print(f"questions example: {prompt + questions}")

        response = client.chat.completions.create(
            model="deepseek-reasoner",
            # model="deepseek-chat",
            messages=messages
        )
        # reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content
        content.replace("```json", "").replace("```", "")

        time.sleep(0.1)
        try:
            answers = json.loads(content)
            opts = answers

            # opts = copy.deepcopy(objs)
            # for idx in range(batch_size):
            #     opts[idx]["output"] = answers[idx]["output"]
            outputs += opts
            if idx < 5 or idx%5 == 0:
                save_json(outputs, output_path)

        except Exception as e:
            # 捕获其他可能的异常
            print(f"发生错误: {e}")
            print(content)
            with open("./datasets/answer_wastes.txt", "a") as wastes:
                wastes.write(content + "\n")
            continue


    save_json(outputs, output_path)

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
    elif analy == "reasoner":
        print("reasoner")
        reasoner(args.file)
    elif analy == "answer_cot":
        print("answer_cot")
        answer_cot(args.file)
    else:
        print("unknown analayse")
        
