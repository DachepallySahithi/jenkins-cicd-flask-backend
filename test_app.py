import unittest
from app import app


class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "success")

    def test_health(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "UP")

    def test_greeting(self):
        response = self.client.get("/api/greet/Sahithi")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json["message"], "Hello, Sahithi!"
        )


if __name__ == "__main__":
    unittest.main()