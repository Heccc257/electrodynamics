import json
import sys
from pathlib import Path

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

    # 创建HTML头部内容，包括引入MathJax并配置为支持内联公式
    html_head = """
<!DOCTYPE html>
<html>
<head>
    <title>Render JSON with LaTeX</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true,  # 允许转义字符
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'],  # 跳过这些标签
                ignoreHtmlClass: 'tex-ignore',  # 忽略带有此类的元素
            },
            svg: {
                fontCache: 'global'
            }
        };
    </script>
    <style>
        body { font-family: Arial, sans-serif; }
        .item { margin-bottom: 20px; border-bottom: 1px solid #ddd; padding-bottom: 10px; }
        .input, .standard, .output { margin: 10px 0; white-space: pre-wrap; word-wrap: break-word; }
    </style>
</head>
<body>
<div id="content">
"""

    # 创建HTML尾部内容
    html_tail = """
</div>
<script>
    // 手动触发 MathJax 渲染
    MathJax.typesetPromise();
</script>
</body>
</html>
"""

    # 将JSON中的每个条目转换为HTML段落，注意转义特殊字符
    html_body = ""
    for item in jsonData:
        html_body += f"""
        <div class="item">
            <div class="input"><strong>Input:</strong> {escape_latex(item.get('input', ''))}</div>
            <div class="standard"><strong>Standard:</strong> {escape_latex(item.get('standard', ''))}</div>
            <div class="output"><strong>Output:</strong> {escape_latex(item.get('output', ''))}</div>
        </div>
        """

    # 组合HTML内容
    html_content = html_head + html_body + html_tail

    # 确定输出文件名
    output_file_path = Path(json_file_path).with_suffix('.html')

    # 写入HTML文件
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML file has been created at: {output_file_path}")
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_filename>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    convert_json_to_html(input_file)