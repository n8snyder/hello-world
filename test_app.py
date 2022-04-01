from unittest import TestCase
from app import app


class HomepageTestCase(TestCase):

    def test_hello_world(self):
        client = app.test_client()
        with client as c:
            response = c.get("/")
            content = response.get_data(as_text=True)

            self.assertEqual(content, "Hello World!")
