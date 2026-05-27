from playwright.sync_api import sync_playwright
import os
import random

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# 1. 生成 8000 到 12000 之间的随机步数
random_steps = random.randint(8000, 12000)
print(f"本次运行生成的随机步数为: {random_steps}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    # 打开网站
    page.goto("http://8.140.250.130/bushu/")

    # 等待页面加载
    page.wait_for_timeout(20000)

    # 输入账号
    page.locator('input[type="text"]').fill(USERNAME)

    # 输入密码
    page.locator('input[type="password"]').fill(PASSWORD)

    # 2. 输入随机步数（将数字转为字符串）
    step_input = page.locator('input[type="number"]')
    step_input.fill(str(random_steps))

    # 3. 填完步数后直接回车提交，彻底解决按钮找不准或点击没反应的问题
    step_input.press("Enter")

    # 等待结果
    page.wait_for_timeout(30000)

    # 保存截图
    page.screenshot(path="result.png")

    browser.close()
