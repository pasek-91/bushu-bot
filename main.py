from playwright.sync_api import sync_playwright
import os
import random

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# 生成 8000 到 12000 之间的随机步数
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

    # 输入随机步数
    step_input = page.locator('input[type="number"]')
    step_input.fill(str(random_steps))

    # 核心修改：明确告诉 Playwright 点击页面上最后一个 button
    # 这样就能避开输入框旁边的小箭头或眼睛图标，直接点中底部的绿色提交按钮
    page.locator("button").last.click()

    # 等待结果
    page.wait_for_timeout(1000)

    # 保存截图
    page.screenshot(path="result.png")

    browser.close()
