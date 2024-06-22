import unittest
import requests
import json
import logging  # Import logging
from pprint import pprint
from utils.custom_test_logger import CustomTestRunner  # Import CustomTestRunner

BASE_URL = 'http://127.0.0.1:5000'
MAX_LOG_LENGTH = 500  # Set maximum length for logging response bodies

class TestDocumentsAPI(unittest.TestCase):

    def log_response_body(self, response):
        self.status_code = response.status_code
        self.response_body = response.content.decode('utf-8')
        if len(self.response_body) > MAX_LOG_LENGTH:
            truncated_body = self.response_body[:MAX_LOG_LENGTH] + '... (truncated)'
        else:
            truncated_body = self.response_body
        logging.debug(f"Status Code: {self.status_code}")
        logging.debug(f"Response Body: {truncated_body}")

    def test_get_all_documents(self):
        response = requests.get(f'{BASE_URL}/documents/')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200)

    def test_create_document(self):
        data = {
            "Type": "Vaccination Record",
            "File": "vaccination_record.pdf"
        }
        response = requests.post(f'{BASE_URL}/documents/', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 201, msg=f"Response content: {response.content}")
        self.doc_id = response.json()['DocID']

    def test_get_document_by_id(self):
        with self.subTest("Ensure a document is created first"):
            self.test_create_document()
        response = requests.get(f'{BASE_URL}/documents/{1}')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

    def test_update_document(self):
        with self.subTest("Ensure a document is created first"):
            self.test_create_document()
        data = {"Type": "Updated Vaccination Record"}
        response = requests.put(f'{BASE_URL}/documents/{1}', data=json.dumps(data), headers={"Content-Type": "application/json"})
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200, msg=f"Response content: {response.content}")

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
