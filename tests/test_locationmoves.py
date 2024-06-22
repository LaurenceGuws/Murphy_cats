import unittest
import requests
import json
import logging  # Import logging
from pprint import pprint
from utils.custom_test_logger import CustomTestRunner  # Import CustomTestRunner
from tests.test_cats import TestCatsAPI

BASE_URL = 'http://127.0.0.1:5000'
MAX_LOG_LENGTH = 500  # Set maximum length for logging response bodies

class TestLocationMovesAPI(unittest.TestCase):

    def log_response_body(self, response):
        self.status_code = response.status_code
        self.response_body = response.content.decode('utf-8')
        if len(self.response_body) > MAX_LOG_LENGTH:
            truncated_body = self.response_body[:MAX_LOG_LENGTH] + '... (truncated)'
        else:
            truncated_body = self.response_body
        logging.debug(f"Status Code: {self.status_code}")
        logging.debug(f"Response Body: {truncated_body}")

    def test_get_all_locationmoves(self):
        response = requests.get(f'{BASE_URL}/locationmoves/')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200)

    def test_create_locationmove(self):
        with self.subTest("Ensure a cat is created first"):
            TestCatsAPI().test_create_cat()
        data = {
            "CatID": 1,
            "FromLocation": "Location A",
            "ToLocation": "Location B",
            "Date": "Tue, 20 Jun 2023 00:00:00 GMT"
        }
        response = requests.post(f'{BASE_URL}/locationmoves/', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 201, msg=f"Response content: {response.content}")
        self.move_id = response.json()['MoveID']

    def test_get_locationmove_by_id(self):
        with self.subTest("Ensure a location move is created first"):
            self.test_create_locationmove()
        response = requests.get(f'{BASE_URL}/locationmoves/{1}')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

    def test_update_locationmove(self):
        with self.subTest("Ensure a location move is created first"):
            self.test_create_locationmove()
        data = {
            "CatID": 1,
            "FromLocation": "Location A",
            "ToLocation": "Location B",
            "Date": "Tue, 20 Jun 2022 00:00:00 GMT"
        }
        response = requests.put(f'{BASE_URL}/locationmoves/{1}', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
