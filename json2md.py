import json
import sys
from pathlib import Path
import re

def escape_latex(text):
    # 转义 HTML 特殊字符，同时保留 LaTeX 公式
    return (
        text.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('$', '&#36;')  # 转义 $ 符号
            .replace('\\', '&#92;')  # 转义 \ 符号
    )

def convert_json_to_html(json_file_path):
    # 读取JSON文件
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            jsonData = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)





    content = ""
    for item in jsonData:
        content += "### intput: \n"
        content += item["input"] + "\n"
        content += "### standard: \n"
        content += item["standard"] + "\n"
        content += "### output: \n"
        content += item["output"] + "\n"
        content += "***\n"

    content = re.sub(r'[\[\]]', '$$', content)
    content = re.sub(r"\\\$\$", "$$", content)

    # 确定输出文件名
    output_file_path = Path(json_file_path).with_suffix('.md')

    # 写入HTML文件
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing md file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_filename>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    convert_json_to_html(input_file)