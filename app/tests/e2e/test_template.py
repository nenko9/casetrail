from playwright.sync_api  import Page


HOST = "http://127.0.0.1:8000"

class TestPageExist:

    def test_open_login_page(self, page:Page):
        page.goto(HOST)


    def test_open_home_page(self, page:Page):
        pass


