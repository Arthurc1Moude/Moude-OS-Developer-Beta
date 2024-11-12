import json
import os
import sys
import subprocess  # 用于执行命令行操作

def release_javascript_project():
    knowledge_base_json = sys.argv[1]
    with open(knowledge_base_json, 'r') as f:
        knowledge_base = json.load(f)

    release_tools_desc = knowledge_base['release']['javascript']['release_tools']['description']
    release_tools_ex = knowledge_base['release']['javascript']['release_tools']['example']

    # 简单示例，假设使用npm进行项目发布，根据描述和示例执行发布操作
    if release_tools_desc == "Use npm for JavaScript project release.":
        release_command = "npm publish"
        try:
            subprocess.run(release_command, shell=True, check=True)
            print("JavaScript项目发布成功。")
        except subprocess.CalledProcessError as e:
            print(f"JavaScript项目发布失败：{e}")

if __name__ == "__main__":
    release_javascript_project()