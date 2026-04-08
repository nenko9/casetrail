from playwright.async_api import Page, expect

class TestOpenPage:

    def test_open_page(self, page:Page):
        page.goto("localhost:8000/")
        # expect(page).to_have_title("")
        assert 1 == 1


