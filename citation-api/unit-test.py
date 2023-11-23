import unittest
from unittest.mock import patch
from flask import Flask
from api import app  # replace 'api' with the actual module name

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('api.os.getenv')
    def test_debug_mode_enabled_in_dev_env(self, mock_getenv):
        mock_getenv.return_value = 'dev'
        with app.app_context():
            self.assertTrue(app.debug)

    @patch('api.os.getenv')
    def test_debug_mode_disabled_in_non_dev_env(self, mock_getenv):
        mock_getenv.return_value = 'prod'
        with app.app_context():
            self.assertFalse(app.debug)

    @patch('api.os.getenv')
    def test_default_port(self, mock_getenv):
        mock_getenv.return_value = None
        with app.app_context():
            self.assertEqual(app.config['SERVER_NAME'], '0.0.0.0:3000')

    def test_hello_world_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    # Add more test cases for other routes and functionality as needed

if __name__ == '__main__':
    unittest.main()
