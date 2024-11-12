import json
import os
import sys
import pycodestyle  # 用于检查JavaScript代码风格，需先安装：pip install pycodestyle

def check_javascript_style():
    knowledge_base_json = sys.argv[1]
    with open(knowledge_base_json, 'r') as f:
        knowledge_base = json.load(f)

    semicolon_usage_desc = knowledge_base['code_style_check']['javascript']['semicolon_usage']['description']
    semicolon_usage_ex = knowledge_base['code_style_check']['javascript']['semicolon_usage']['example']
    brace_style_desc = knowledge_base['code_style_check']['javascript']['brace_style']['description']
    brace_style_ex = knowledge_base['code_style_check']['javascript']['brace_style']['example']
    spacing_and_formatting_desc = knowledge_base['code_style_check']['javascript']['spacing_and_formatting']['description']
    spacing_and_formatting_ex = knowledge_base['code_style_check']['javascript']['spacing_and_formatting']['example']

    js_files = [f for f in os.listdir('.') if f.endswith('.js')]

    style_guide = pycodestyle.StyleGuide()

    for js_file in js_files:
        with open(js_file, 'r') as f:
            code = f.read()

        # 分号使用检查逻辑
        if semicolon_usage_desc == "Use semicolons consistently in JavaScript.":
            errors = style_guide.input_file(js_file, check_semicolons=True)
            if errors:
                print(f"{js_file} 中存在分号使用不规范的情况：")
                for error in errors:
                    print(error)

        # 大括号风格检查逻辑
        if brace_style_desc == "Choose a brace style and be consistent.":
            # 简单示例，检查大括号是否在同一行（假设简单情况）
            brace_lines = []
            for i, line in enumerate(code.splitlines()):
                if "{" in line:
                    brace_lines.append(i)
                if "}" in line:
                    brace_lines.append(i)
            if len(brace_lines) % 2!= 0:
                print(f"{js_file} 大括号不匹配。")
            else:
                for i in range(0, len(brace_lines), 2):
                    if brace_lines[i + 1] - brace_lines[i]!= 1:
                        print(f"{js_file} 大括号风格不一致。")

        # 间距和格式化检查逻辑
        if spacing_and_formatting_desc == "Use consistent spacing around operators and after commas. Keep the code formatting clean.":
            # 简单示例，检查运算符前后间距（假设简单判断）
            operators = ["+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||"]
            for operator in operators:
                if operator + " " not in code and " " + operator not in code:
                    print(f"{js_file} 中运算符 {operator} 前后间距不一致。")

if __name__ == "__main__":
    check_javascript_style()