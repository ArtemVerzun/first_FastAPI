from unittest import TestCase
from fastapi.testclient import TestClient

from main import app as web_app


class TestAPICase(TestCase):

    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        user_data = {
            'user': {
                'email': 'test2@test.com',
                'password': '1234',
                'first_name': 'Artem2',
                'last_name': 'Verzun2',
                'nickname': 'va2'
            }
        }

        response = self.client.post('/user', json=user_data)
        self.assertEqual(response.status_code, 200)
