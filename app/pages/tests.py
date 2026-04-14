from django.test import TestCase, Client
from django.urls import reverse


class TestPagesDirectLink(TestCase):
    def setUp(self):
        self.client = Client()

    def test_open_login_page(self):
        response = self.client.get(path=reverse("login"))
        self.assertEqual(
            response.status_code,
            200,
            "Login page response status code error %s" % response.status_code,
        )
        self.assertContains(response, "Login")

    def test_open_wellcome_page(self):
        response = self.client.get(path=reverse("wellcome"))
        self.assertEqual(
            response.status_code,
            200,
            "Wellcome page response status code error %s" % response.status_code,
        )
        self.assertContains(response, "Wellcome page")
