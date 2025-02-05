import requests
from openai import OpenAI
api_key = "sk-ceajxtcicytniffxkfcwfsqgyokeqnyxdctctrkongnnogxl"
url = "https://api.siliconflow.cn/v1/chat/completions"

def ask_silicon(question):

    prompt = "解决下面的电动力学问题，同时可能给出参考答案，简要给出详细的数学推导和计算过程，思考过程用<think> </think>包裹，答案用<answer> </answer>包裹。公式使用latex格式，用$包裹\n\n" + question + "\n\n"
    
    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        # "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "stream": False,
        "stop": ["null"],
        "temperature": 0.0,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.request("POST", url, json=payload, headers=headers, timeout=(3, 300000))
    except requests.exceptions.ReadTimeout:
        return "timeout"
    if response.status_code != 200:
        return response.text
    
    return response.json().get("choices")[0].get("message").get("content")
    
if __name__ == "__main__":
    print(ask_silicon("计算一个均匀极化的无限大介质板的面束缚电荷密度。假设极化强度为 $\\mathbf{P} = P_0 \\hat{z}$，介质板的法向量为 $\\hat{n} = \\hat{z}$。"))

