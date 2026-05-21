![API Tests](https://github.com/shristi310/API-TEST-PROJECT/actions/workflows/tests.yml/badge.svg)


# API Test Suite — JSONPlaceholder

Automated REST API testing project built with Python and pytest.

## Tools Used
- Python 3.10
- pytest
- requests
- pytest-html
- GitHub Actions

## What is Tested
- Posts API (GET, POST, PUT, DELETE)
- Users API (GET, validate structure)
- Comments API (GET, validate structure)
- Status codes, data types, response time

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run all tests
pytest -v

### Generate HTML report
pytest -v --html=report.html --self-contained-html

## Test Results
- 22 test cases
- All passing ✅