import json
import os
import sys
import subprocess  # 用于执行命令行操作

def build_javascript_project():
    knowledge_base_json = sys.argv[1]
    with open(knowledge_base_json, 'r') as f:
        knowledge_base = json.load(f)

    build_tools_desc = knowledge_base['project_build']['javascript']['build_tools']['description']
    build_tools_ex = knowledge_base['project_build']['javascript']['build_tools']['example']
    minification_desc = knowledge_base['project_build']['javascript']['minification']['description']
    minification_ex = knowledge_base['project_build']['javascript']['minification']['example']
    source_maps_desc = knowledge_base['project_build']['javascript']['source_maps']['description']
    source_maps_ex = knowledge_base['project_build']['javascript']['source_maps']['example']

    # 假设使用Webpack作为构建工具，根据示例配置进行构建
    if build_tools_desc == "Use Webpack or Rollup for JavaScript builds. Webpack bundles files and dependencies.":
        webpack_config_path = "webpack.config.js"  # 假设Webpack配置文件名为webpack.config.js
        # 检查Webpack配置文件是否存在
        if not os.path.exists(webpack_config_path):
            print(f"Webpack配置文件 {webpack_config_path} 不存在。")
            return

        # 执行Webpack构建命令
        build_command = ["webpack", "--config", webpack_config_path]
        if minification_desc == "Minify JavaScript with tools like UglifyJS during build for smaller size.":
            build_command.append("--optimize-minimize")
        if source_maps_desc == "Generate source maps during the build process to help with debugging in production environments.":
            build_command.append("--devtool=source-map")

        try:
            subprocess.run(build_command, check=True)
            print("JavaScript项目构建成功。")
        except subprocess.CalledProcessError as e:
            print(f"JavaScript项目构建失败：{e}")

if __name__ == "__main__":
    build_javascript_project()