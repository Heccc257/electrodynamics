import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-90db01b7652f459bb3295de1aac85967", # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def ask_aliyun(question):
    completion = client.chat.completions.create(
        model="qwen-plus", # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        # model="qwq-32b-preview", # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        # model="deepseek-v3",
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': question},
        ],
        temperature=0.1,
    )
    # print(completion)
    # print(completion.keys())
    return completion.choices[0].message.content

if __name__ == "__main__":
    print(ask_aliyun("计算一个均匀极化的无限大介质板的面束缚电荷密度。假设极化强度为 $\\mathbf{P} = P_0 \\hat{z}$，介质板的法向量为 $\\hat{n} = \\hat{z}$。"))

