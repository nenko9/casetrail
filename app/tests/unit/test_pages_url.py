from django.test import TestCase, Client

class TestOpenPage(TestCase):

    def test_open_page(self, pages):
        """
        Test that the opened page return correct status code and page exit.
        :param pages:
        :return:22
        """
        client = Client()
        for page in pages:
            response = client.get(page)
            assert response.status_code == 200

