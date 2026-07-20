import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.c = app.test_client()

    def test_api_list(self):
        r = self.c.get("/api/courses")
        self.assertEqual(r.status_code, 200)
        self.assertGreaterEqual(len(r.get_json()), 6)

    def test_api_detail_ok(self):
        r = self.c.get("/api/courses/1")
        self.assertEqual(r.status_code, 200)
        self.assertIn("id", r.get_json())

    def test_api_detail_missing(self):
        r = self.c.get("/api/courses/9999")
        self.assertEqual(r.status_code, 404)

    def test_list_page(self):
        r = self.c.get("/")
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()
