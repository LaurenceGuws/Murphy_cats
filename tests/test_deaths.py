import unittest
import requests
import json
import logging  # Import logging
from pprint import pprint
from utils.custom_test_logger import CustomTestRunner  # Import CustomTestRunner
from tests.test_cats import TestCatsAPI

BASE_URL = 'http://127.0.0.1:5000'
MAX_LOG_LENGTH = 500  # Set maximum length for logging response bodies

class TestDeathsAPI(unittest.TestCase):

    def log_response_body(self, response):
        self.status_code = response.status_code
        self.response_body = response.content.decode('utf-8')
        if len(self.response_body) > MAX_LOG_LENGTH:
            truncated_body = self.response_body[:MAX_LOG_LENGTH] + '... (truncated)'
        else:
            truncated_body = self.response_body
        logging.debug(f"Status Code: {self.status_code}")
        logging.debug(f"Response Body: {truncated_body}")

    def test_get_all_deaths(self):
        response = requests.get(f'{BASE_URL}/deaths/')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200)

    def test_create_death(self):
        with self.subTest("Ensure a cat is created first"):
            TestCatsAPI().test_create_cat()
        data = {
            "CatID": 1,
            "CauseOfDeath": "Accident",
            "VetName": "Dr. Brown",
            "Date": "Tue, 20 Jun 2023 00:00:00 GMT",
            "Location": "Location C"
        }
        response = requests.post(f'{BASE_URL}/deaths/', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 201, msg=f"Response content: {response.content}")
        self.death_id = response.json()['DeathID']

    def test_get_death_by_id(self):
        with self.subTest("Ensure a death is created first"):
            self.test_create_death()
        response = requests.get(f'{BASE_URL}/deaths/{1}')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

    def test_update_death(self):
        with self.subTest("Ensure a death is created first"):
            self.test_create_death()
        data = {
            "CatID": 1,
            "CauseOfDeath": "Accident2",
            "VetName": "Dr. Brown",
            "Date": "Tue, 20 Jun 2023 00:00:00 GMT",
            "Location": "Location C"
        }
        response = requests.put(f'{BASE_URL}/deaths/{1}', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
