import json
import os
import sys
import requests  # 用于模拟请求等操作，需先安装：pip install requests

def check_javascript_security():
    knowledge_base_json = sys.argv[1]
    with open(knowledge_base_json, 'r') as f:
        knowledge_base = json.load(f)

    xss_prevention_desc = knowledge_base['security_check']['javascript']['xss_prevention']['description']
    xss_prevention_ex = knowledge_base['security_check']['javascript']['xss_prevention']['example']
    csrf_prevention_desc = knowledge_base['security_check']['javascript']['csrf_prevention']['description']
    csrf_prevention_ex = knowledge_base['security_check']['javascript']['csrf_prevention']['example']
    secure_cookie_usage_desc = knowledge_base['security_check']['javascript']['secure_cookie_usage']['description']
    secure_cookie_usage_ex = knowledge_base['security_check']['javascript']['secure_cookie_usage']['example']

    js_files = [f for f in os.listdir('.') if f.endswith('.js')]

    for js_file in js_files:
        with open(js_file, 'r') as f:
            code = f.read()

        # 跨站脚本攻击（XSS）预防检查逻辑
        if xss_prevention_desc == "Sanitize user input in JavaScript to prevent XSS, e.g., with DOMPurify.":
            # 简单示例，检查是否调用了类似DOMPurify的函数来净化输入（假设已知函数名）
            if "DOMPurify" not in code:
                print(f"{js_file} 可能存在XSS风险，未使用DOMPurify净化输入。")

        # 跨站请求伪造（CSRF）预防检查逻辑
        if csrf_prevention_desc == "Use CSRF tokens in JavaScript AJAX requests.":
            # 简单示例，检查AJAX请求中是否包含CSRF令牌（假设简单判断）
            if "XMLHttpRequest" in code or "fetch" in code:
                if "csrf_token" not in code:
                    print(f"{js_file} 可能存在CSRF风险，AJAX请求中未包含CSRF令牌。")

        # 安全Cookie使用检查逻辑
        if secure_cookie_usage_desc == "Set the'secure' and 'httpOnly' flags on cookies to enhance security.":
            # 简单示例，检查是否设置了secure和httpOnly属性（假设简单判断）
            if "document.cookie" in code:
                if "secure" not in code or "httpOnly" not in code:
                    print(f"{js_file} 中Cookie设置可能不安全，未设置secure和httpOnly属性。")

if __name__ == "__main__":
    check_javascript_security()