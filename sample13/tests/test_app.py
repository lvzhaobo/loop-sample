import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_200(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_index_contains_header(self):
        resp = self.client.get('/')
        self.assertIn(b'20260723-Loop', resp.data)

    def test_index_contains_footer(self):
        resp = self.client.get('/')
        self.assertIn(b'Loop-20260723', resp.data)


if __name__ == '__main__':
    unittest.main()