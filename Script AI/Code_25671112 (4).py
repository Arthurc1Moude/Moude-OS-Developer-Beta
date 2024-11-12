import json
import os
import sys

def test_javascript_project():
    knowledge_base_json = sys.argv[1]
    with open(knowledge_base_json, 'r') as f:
        knowledge_base = json.load(f)

    testing_framework_desc = knowledge_base['testing']['javascript']['testing_framework']['description']
    testing_framework_ex = knowledge_base['testing']['javascript']['testing_framework']['example']

    # 简单示例，假设使用Jest作为测试框架，根据描述和示例执行测试
    if testing_framework_desc == "Use Jest for JavaScript testing.":
        test_command = "jest"  # 假设Jest测试命令为jest
        try:
            os.system(test_command)
        except Exception as e:
            print(f"JavaScript项目测试失败：{e}")

if __name__ == "__main__":
    test_javascript_project()