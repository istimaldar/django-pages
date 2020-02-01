from django.test import TestCase, SimpleTestCase


class SimpleTest(SimpleTestCase):
    def test_main_page(self):
        self.assertEqual(self.client.get('/').status_code, 200)

    def test_about_page(self):
        self.assertEqual(self.client.get('/about/').status_code, 200)
