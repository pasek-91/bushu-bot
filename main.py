from playwright.sync_api import sync_playwright
import os
import random
import time

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

STEP = random.randint(15000, 25000)

URL = "http://8.140.250.130/bushu/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    print("打开网站...")
    page.goto(URL, timeout=60000)

    time.sleep(2)

    print("输入账号...")
    page.locator('input[type="text"]').fill(USERNAME)

    print("输入密码...")
    page.locator('input[type="password"]').fill(PASSWORD)

    print("输入步数...")
    number_input = page.locator('input[type="number"]')
    number_input.fill(str(STEP))

    time.sleep(1)

    print(f"提交步数：{STEP}")

    page.get_by_role("button", name="出去走走").click()

    time.sleep(5)

    # 保存截图
    page.screenshot(path="result.png")

    print("执行完成")

    browser.close()    page.get_by_role("button", name="出去走走").click()

    time.sleep(5)

    page.screenshot(path="result.png")

    print("执行完成")

    browser.close()
