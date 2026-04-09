from django.test import Client
from django.urls import reverse


class TestOpenPage:

    def test_open_page(self, pages):
        """
        Test that the opened page return correct status code and page exit.
        :param pages:
        :return:22
        """
        client = Client()
        for page in pages:
            url = reverse(page)
            response = client.get(url)
            assert response.status_code == 200, f"URL not found {page}"
