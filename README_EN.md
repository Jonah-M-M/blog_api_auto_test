# Blog‑System API Automation Test（Based on requests and pytest）
> 📖 本文档为英文版，如需阅读中文版本，请点击 **[中文版本](./README.md)**
## Project Introduction
This project implements API automation testing for blog backend system based on Requests + Pytest.
It covers full positive and abnormal test scenarios for the login module.
Secondary encapsulation of requests provides unified request processing and full‑link log embedding.
YAML is used for data‑driven testing, and JsonSchema performs strict validation on response JSON structure.
A singleton logging component built with logging module outputs logs to console, info log file and error log file separately for fast troubleshooting. Allure is supported to generate visual test reports.

## Environment Requirements
- Python >= 3.8
- Network access to the tested blog backend API service
## How to Run Tests
```bash
pytest Test/ -v
pytest Test/ --alluredir=allure-results
allure generate allure-results -o allure-report --clean
```
## Project Directory Structure
```
blog_api_auto/
├── Test/                      # Business test case directory
│   └── test_login_api_auto.py # Login module API test cases
├── utils/                     # Common utility module
│   ├── __init__.py
│   ├── logging_util.py        # Singleton logger wrapper
│   └── request_util.py        # Encapsulated requests client
├── data/                      # YAML test data directory
│   └── login_cases.yaml       # Test data for login scenarios
├── logs/                      # Auto‑generated log directory
├── pytest.ini                 # Global pytest configuration
├── requirements.txt           # Third‑party dependency list
└── README.md                  # Chinese project documentation
```

## Test Case Design
Test cases are designed according to official API documentation.
Covers login success scenario, plus invalid cases: empty username, empty password, wrong username & password.
@pytest.mark.parametrize is adopted for data‑driven implementation.
Further extension supports article publish, query, privilege‑overrun test and other business interfaces.
## Notes
1. The logs folder will be created automatically during runtime, no manual creation required.
2. The target blog service is a public test server. Network jitter, rate‑limit and response delay are expected external‑environment behaviors.
3. All test commands must run under project root directory, otherwise module import or case collection failures will occur.
4. logs, allure‑results, allure‑report are runtime output directories. Add them to gitignore and do NOT commit to repository.
5. Replace API addresses in source code with real service endpoints, otherwise test cases cannot execute normally.
