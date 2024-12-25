# Python Selenium Framework

This repository contains a Python-based Selenium automation framework. It demonstrates the basics of web automation using **Selenium WebDriver**, **Python**, and **pytest**. The framework is designed to be easily extendable for more advanced web testing and automation tasks in the future.

## Project Overview

This project uses Selenium WebDriver for automating web interactions, organized using the **Page Object Model (POM)** pattern. The framework is built to test web applications, specifically using form submission and end-to-end tests. Data-driven testing is also implemented with **pytest** fixtures.

### Key Features:
- **Page Object Model (POM)**: The framework uses POM for better test maintainability and reusability.
- **End-to-End Testing**: Automated end-to-end flow for adding items to the cart, checkout, and order confirmation.
- **Data-Driven Testing**: Uses `pytest` fixtures with external test data for parameterized testing.
- **Test Reports**: Generates HTML reports after test execution.
- **Logging**: Detailed logging during test execution for easy debugging.

## Prerequisites

Before running the tests, ensure that you have the following installed:
- Python 3.x
- Selenium
- WebDriver Manager for Chrome
- pytest

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/nbezverkhaya/PythonSeleniumFramework.git
    ```

2. Navigate to the project directory:
    ```bash
    cd PythonSeleniumFramework
    ```

3. Create a virtual environment (if not already created):
    ```bash
    python -m venv .venv
    ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Make sure to configure the WebDriver Manager and ensure ChromeDriver is properly set up. This is automatically handled by the `webdriver-manager` library.

## Running the Tests

To run the tests, you can use `pytest`. In the terminal, navigate to the project directory and run:

```bash
pytest
This will automatically discover and run all the tests.

Running Specific Test
To run a specific test, use the following command:

bash

pytest -k 'test_formSubmission'
Replace test_formSubmission with the name of the test you want to execute.

**Contributing**  
Feel free to open issues or create pull requests if you'd like to contribute to this project.

**License**  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Folder Structure
Here is a brief overview of the project structure:

.
├── .venv/                          # Virtual environment directory
│   ├── bin/                         # Executables
│   ├── lib/                         # Libraries
│   ├── .gitignore                   # Git ignore file for virtual environment
│   └── pyvenv.cfg                   # Python virtual environment configuration
├── pageObject/                     # Page Object Model (POM) files
│   ├── __init__.py                  # Initialization file
│   ├── Checkout.py                  # Page object for Checkout page
│   ├── Confirm.py                   # Page object for Confirm page
│   └── Home.py                      # Page object for Home page
├── reports/                         # Test reports
│   ├── assets/                      # Report assets (images, etc.)
│   ├── __init__.py                  # Initialization file
│   └── report.html                  # Generated test report
├── TestData/                        # Test data
│   ├── __init__.py                  # Initialization file
│   ├── exelDemo.py                  # Example test data script
│   ├── HomePageData.py              # Test data for Home page tests
│   ├── PythonDemo2.numbers          # Test data (Numbers file)
│   └── PythonDemo2.xlsx             # Test data (Excel file)
├── tests/                           # Test cases
│   ├── assets/                      # Test assets (e.g., images, files)
│   ├── __init__.py                  # Initialization file
│   ├── conftest.py                  # pytest configuration file
│   ├── logfile.log                  # Log file generated during test execution
│   ├── test_e2e.py                  # End-to-end test case
│   └── test_HomePage.py             # Home page test case
├── utilities/                       # Utility functions
│   ├── __init__.py                  # Initialization file
│   └── BaseClass.py                 # Base class for common functionality
├── .gitignore                       # Git ignore file
├── mynotes.txt                      # Notes file
└── README.md                        # Project documentation
