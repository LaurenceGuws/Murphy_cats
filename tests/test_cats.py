import random
import unittest
import requests
import json
import logging  # Import logging
from pprint import pprint
from utils.custom_test_logger import CustomTestRunner  # Import CustomTestRunner

BASE_URL = 'http://127.0.0.1:5000'
MAX_LOG_LENGTH = 500  # Set maximum length for logging response bodies

class TestCatsAPI(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test method is executed.
        some_value = random.randint(1, 1000)
        self.cat_id = some_value  # Ensure this value is correctly initialized

    def log_response_body(self, response):
        self.status_code = response.status_code
        self.response_body = response.content.decode('utf-8')
        if len(self.response_body) > MAX_LOG_LENGTH:
            truncated_body = self.response_body[:MAX_LOG_LENGTH] + '... (truncated)'
        else:
            truncated_body = self.response_body
        logging.debug(f"Status Code: {self.status_code}")
        logging.debug(f"Response Body: {truncated_body}")

    def test_get_all_cats(self):
        response = requests.get(f'{BASE_URL}/cats/')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200)

    def test_create_cat(self):
        data = {
            "AdoptedDate": "Wed, 01 Jan 2020 00:00:00 GMT",
            "AdopterID": 1,
            "BirthDate": "Wed, 01 Jan 2018 00:00:00 GMT",
            "Colour": "Brown",
            "Condition": "Healthy",
            "CurrentLocation": "Location A",
            "FirstVax": "Sun, 01 Mar 2020 00:00:00 GMT",
            "Name": "Whiskers",
            "ReceivedDate": "Wed, 01 Jan 2020 00:00:00 GMT",
            "SecondVax": "Wed, 01 Apr 2020 00:00:00 GMT",
            "Sex": "Female",
            "SteriDue": "Fri, 01 Jan 2021 00:00:00 GMT",
            "Weight": 4.5
        }
        response = requests.post(f'{BASE_URL}/cats/', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 201, msg=f"Response content: {response.content}")
        self.cat_id = response.json()['CatID']

    def test_get_cat_by_id(self):
        with self.subTest("Ensure a cat is created first"):
            self.test_create_cat()
        response = requests.get(f'{BASE_URL}/cats/{1}')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

    def test_update_cat(self):
        with self.subTest("Ensure a cat is created first"):
            self.test_create_cat()
        data = {
            "AdoptedDate": "Wed, 01 Jan 2020 00:00:00 GMT",
            "AdopterID": 1,
            "BirthDate": "Wed, 01 Jan 2018 00:00:00 GMT",
            "Colour": "Brown",
            "Condition": "Healthy2",
            "CurrentLocation": "Location A",
            "FirstVax": "Sun, 01 Mar 2020 00:00:00 GMT",
            "Name": "Whiskers",
            "ReceivedDate": "Wed, 01 Jan 2020 00:00:00 GMT",
            "SecondVax": "Wed, 01 Apr 2020 00:00:00 GMT",
            "Sex": "Female",
            "SteriDue": "Fri, 01 Jan 2021 00:00:00 GMT",
            "Weight": 4.5
        }
        response = requests.put(f'{BASE_URL}/cats/{1}', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
