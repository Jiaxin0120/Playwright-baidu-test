from playwright.sync_api import sync_playwright,expect
import random
import time

#单关键词搜索测试
def test_baiduSearch_singleKeyword():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False,slow_mo=200)
        page = browser.new_page()
        page.goto("https://www.baidu.com", timeout=20000)

        page.wait_for_timeout(random.randint(1000, 1500))
        search_box = page.locator("#chat-textarea")#搜索框id
        expect(search_box, "搜索框不可见").to_be_visible(timeout=10000)
        expect(search_box, "搜索框不可编辑").to_be_editable()
        search_box.fill("Playwright")

        page.wait_for_timeout(random.randint(500, 1000))
        expect(page.locator("#chat-submit-button"), "搜索按钮失效").to_be_enabled()#搜索按钮id
        page.locator("#chat-submit-button").click()
        page.wait_for_selector("#content_left",timeout=10000)
        search_results=page.locator("#content_left")#搜索结果id
        time.sleep(2)
        assert search_results.is_visible(),"Not visible"
        assert search_results.inner_text()!=None,"No results"
        page.screenshot(path="Search_singleKeyword.png")
        browser.close()

#空值搜索测试
def test_baiduSearchNone():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=200)
        page = browser.new_page()
        page.goto("https://www.baidu.com", timeout=20000)

        page.wait_for_timeout(random.randint(500, 1000))
        search_box = page.locator("#chat-textarea")

        expect(search_box, "搜索框不可见").to_be_visible(timeout=10000)
        expect(search_box, "搜索框不可编辑").to_be_editable()
        search_box.fill("")

        page.wait_for_timeout(random.randint(500, 1000))
        expect(page.locator("#chat-submit-button"), "搜索按钮失效").to_be_enabled()
        page.locator("#chat-submit-button").click()
        page.wait_for_selector("#content_left", timeout=10000)
        search_results = page.locator("#content_left")
        time.sleep(2)
        assert search_results.is_visible(), "Not visible"
        assert search_results.inner_text() != None, "No results"
        page.screenshot(path="Search_None.png")
        browser.close()

if __name__ == "__main__":
    test_baiduSearch_singleKeyword()
    test_baiduSearchNone()