Here is the updated `README` file with the additional context about the project:

---

# Murphy Cats

## Overview

Murphy Cats is a project designed to support a group of dedicated volunteers who shelter cats in need in Benoni, Gauteng. This project includes an API for managing various aspects of the cat adoption and foster care process, such as handling adopters, cats, volunteers, vet visits, location moves, deaths, and documents. The project also features automated tests to ensure the API functions correctly.

## Features

- Manage adopters, cats, and volunteers.
- Track vet visits, location moves, and deaths.
- Handle documents related to cat adoption and foster care.
- Automated tests with detailed logging.

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)
- `virtualenv` (Recommended for creating a virtual environment)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Murphy_cats.git
    cd Murphy_cats
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv cat_foster_env
    source cat_foster_env/bin/activate  # On Windows, use `cat_foster_env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the API

To start the API, run the following command:

```bash
flask run
```

The API will be available at `http://127.0.0.1:5000`.

## Running Tests

The project includes a comprehensive suite of automated tests. To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Project Structure

- `app/`: Contains the main application code.
- `tests/`: Contains the automated tests.
- `utils/`: Contains utility modules, including the custom test logger.
- `requirements.txt`: Lists the Python dependencies.

## Custom Logging

The project uses a custom test logger located in `utils/custom_test_logger.py` for detailed logging of test results.

### Logging Configuration

- Logs are saved to `tests/test_results.log`.
- Detailed logs, including response bodies, are saved to `tests/full_test_log.log`.
- Only the test name and status code are displayed in the terminal during test execution.

### Example Test File

Below is an example of how to set up a test file to use the custom logger:

```python
import random
import unittest
import requests
import json
import logging  # Import logging
from pprint import pprint
from utils.custom_test_logger import CustomTestRunner  # Import CustomTestRunner

BASE_URL = 'http://127.0.0.1:5000'
MAX_LOG_LENGTH = 500  # Set maximum length for logging response bodies

class TestExampleAPI(unittest.TestCase):

    def log_response_body(self, response):
        self.status_code = response.status_code
        self.response_body = response.content.decode('utf-8')
        if len(self.response_body) > MAX_LOG_LENGTH:
            truncated_body = self.response_body[:MAX_LOG_LENGTH] + '... (truncated)'
        else:
            truncated_body = self.response_body
        logging.debug(f"Status Code: {self.status_code}")
        logging.debug(f"Response Body: {truncated_body}")

    def test_example(self):
        response = requests.get(f'{BASE_URL}/example/')
        self.log_response_body(response)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner)
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.