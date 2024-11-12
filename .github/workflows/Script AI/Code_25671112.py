import json
import os
import sys
import jsbeautifier  # 用于格式化JavaScript代码，需先安装：pip install jsbeautifier

def optimize_javascript_code():
    knowledge_base_json = sys.argv[1]
    with open(knowledge_base_json, 'r') as f:
        knowledge_base = json.load(f)

    variable_declaration_desc = knowledge_base['code_optimization']['javascript']['variable_declaration']['description']
    variable_declaration_ex = knowledge_base['code_optimization']['javascript']['variable_declaration']['example']
    function_definition_desc = knowledge_base['code_optimization']['javascript']['function_definition']['description']
    function_definition_ex = knowledge_base['code_optimization']['javascript']['function_definition']['example']
    loop_optimization_desc = knowledge_base['code_optimization']['javascript']['loop_optimization']['description']
    loop_optimization_ex = knowledge_base['code_optimization']['javascript']['loop_optimization']['example']
    memory_management_desc = knowledge_base['code_optimization']['javascript']['memory_management']['description']
    memory_management_ex = knowledge_base['code_optimization']['javascript']['memory_management']['example']

    # 获取当前目录下所有的.js文件
    js_files = [f for f in os.listdir('.') if f.endswith('.js')]

    for js_file in js_files:
        with open(js_file, 'r') as f:
            original_code = f.read()

        # 变量声明优化逻辑
        if variable_declaration_desc == "Use 'let' or 'const' instead of 'var'.":
            original_code = original_code.replace("var ", "let ")

        # 函数定义优化逻辑
        if function_definition_desc == "Prefer arrow functions, e.g., const add = (a, b) => a + b;":
            # 简单示例，将普通函数转换为箭头函数（假设函数定义符合简单情况）
            while True:
                start_index = original_code.find("function ")
                if start_index == -1:
                    break
                end_index = original_code.find("(", start_index)
                function_name = original_code[start_index + 8:end_index]
                params_end_index = original_code.find(")", end_index)
                params = original_code[end_index + 1:params_end_index]
                body_start_index = original_code.find("{", params_end_index)
                body_end_index = original_code.find("}", body_start_index)
                body = original_code[body_start_index + 1:body_end_index]
                arrow_function = f"const {function_name} = ({params}) => {body}"
                original_code = original_code[:start_index] + arrow_function + original_code[body_end_index + 1:]

        # 循环优化逻辑
        if loop_optimization_desc == "Minimize nested loops; consider array methods like map, filter, reduce for better performance.":
            # 简单示例，将简单的for循环转换为map（假设符合特定条件）
            while True:
                start_index = original_code.find("for (")
                if start_index == -1:
                    break
                end_index = original_code.find(")", start_index)
                for_loop = original_code[start_index:end_index + 1]
                if "map" not in for_loop and "filter" not in for_loop and "reduce" not in for_loop:
                    variable_declaration = for_loop.split(";")[0].split(" ")[1]
                    condition = for_loop.split(";")[1].strip()
                    increment = for_loop.split(";")[2].strip()
                    loop_body = original_code[end_index + 1:original_code.find("}", end_index)].strip()
                    map_expression = f"{variable_declaration}.map(({variable_declaration}) => {loop_body})"
                    original_code = original_code[:start_index] + map_expression + original_code[original_code.find("}", end_index) + 1:]

        # 内存管理优化逻辑
        if memory_management_desc == "Avoid creating unnecessary closures as they can hold references and consume memory. Also, use local variables inside functions instead of relying on global scope.":
            # 简单示例，检查并移除不必要的闭包（假设可以通过简单判断识别）
            while True:
                start_index = original_code.find("(function() {")
                if start_index == -1:
                    break
                end_index = original_code.find("})();", start_index)
                closure = original_code[start_index:end_index + 4]
                if "return function" not in closure:
                    original_code = original_code[:start_index] + original_code[end_index + 4:]

        # 使用jsbeautifier格式化优化后的代码
        optimized_code = jsbeautifier.beautify(original_code)

        with open(js_file, 'w') as f:
            f.write(optimized_code)

if __name__ == "__main__":
    optimize_javascript_code()