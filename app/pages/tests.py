from django.test import TestCase, Client

PAGE = {
    "login":"login/",
}

class TestPagesDirectLink(TestCase):
    def test_open_login_page(self):
        client = Client()
        response = client.get(path="/login/")
        self.assertEqual(response.status_code, 200, "Login page response status code error %s" %response.status_code)

