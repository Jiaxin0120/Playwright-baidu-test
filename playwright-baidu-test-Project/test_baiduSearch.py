from playwright.sync_api import sync_playwright,expect
import random

#单关键词搜索测试
def test_baiduSearch_singleKeyword():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False,slow_mo=200)
        page = browser.new_page()
        page.goto("https://www.baidu.com", timeout=20000)

        page.wait_for_timeout(random.randint(1000, 1500))
        search_box = page.locator("#kw")##kw稳定定位器
        expect(search_box, "搜索框不可见").to_be_visible(timeout=10000)
        expect(search_box, "搜索框不可编辑").to_be_editable()
        search_box.fill("Playwright")

        page.wait_for_timeout(random.randint(500, 1000))
        expect(page.locator("#su"), "搜索按钮失效").to_be_enabled()##su稳定定位器
        page.locator("#su").click()
        page.wait_for_selector("#content_left",timeout=10000)
        search_results=page.locator("#content_left")
        assert search_results.is_visible(),"Not visible"
        assert search_results.inner_text()!=None,"No results"
        page.screenshot(path="example.png")
        browser.close()

#空值搜索测试
def test_baiduSearchNone():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=200)
        page = browser.new_page()
        page.goto("https://www.baidu.com", timeout=20000)

        page.wait_for_timeout(random.randint(500, 1000))
        search_box = page.locator("#kw")  ##kw稳定定位器

        expect(search_box, "搜索框不可见").to_be_visible(timeout=10000)
        expect(search_box, "搜索框不可编辑").to_be_editable()
        search_box.fill("")

        page.wait_for_timeout(random.randint(500, 1000))
        expect(page.locator("#su"), "搜索按钮失效").to_be_enabled()
        page.locator("#su").click()
        expect(page).to_have_title("百度一下，你就知道")
        browser.close()

if __name__ == "__main__":
    test_baiduSearch_singleKeyword()
    test_baiduSearchNone()