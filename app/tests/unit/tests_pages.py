from django.test import TestCase, Client
import allure


# Create your test here.
class TestPages(TestCase):

    @allure.title('Test root page')
    def test_root_page(self):

        with allure.step("Test pre-setup"):
            client  = Client()
            response = client.get("/")

        with allure.step("Verify root page"):
            assert response.status_code == 200