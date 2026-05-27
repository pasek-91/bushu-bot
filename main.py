from playwright.sync_api import sync_playwright
import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page()

    # 打开网站
    page.goto("你的网站链接")

    # 等待页面加载
    page.wait_for_timeout(3000)

    # 输入账号
    page.locator('input[type="text"]').fill(USERNAME)

    # 输入密码
    page.locator('input[type="password"]').fill(PASSWORD)

    # 输入步数
    page.locator('input[type="number"]').fill("30000")

    # 点击按钮
    page.get_by_role("button", name="出去走走").click()

    # 等待完成
    page.wait_for_timeout(5000)

    print("执行完成")

    browser.close()
