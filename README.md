# QA Automation Assistant

## Project Overview

QA Automation Assistant is a prototype that demonstrates how AI can support software testing by converting manual test cases into Selenium automation script templates.

The project addresses a common challenge faced by QA teams: transforming manual test scenarios into automation scripts. This proof-of-concept provides a simple interface where users can enter a manual test case and receive a generated Selenium script.

## Problem Statement

Writing automation scripts from manual test cases can be repetitive and time-consuming. QA Engineers and Automation Testers often spend significant time converting test steps into code before automation testing can begin.

## Intended Users

- QA Analysts
- Test Automation Engineers
- Software Testing Teams

## Features

- User-friendly web interface built with Streamlit
- Accepts manual QA test cases as input
- Generates Selenium automation script templates
- Demonstrates AI-assisted test automation concepts

## Technology Stack

- Python
- Streamlit
- Selenium (generated output examples)

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the application:

```bash
streamlit run app.py
```

## Example Input

```text
Verify a user can successfully log into the application using valid credentials.

1. Navigate to Login Page
2. Enter Username
3. Enter Password
4. Click Login
5. Verify Dashboard displays
```

## Example Output

The application generates a Selenium automation script template based on the provided manual test case.

## AI Functionality

This prototype demonstrates how AI-assisted tools can help generate automation script templates from manual test cases. The current version serves as a proof of concept and foundation for future integration with a large language model (LLM).

## Limitations

- Generated scripts may require modification before use.
- Human review is required before using generated scripts in production environments.

## Future Enhancements

- Integration with OpenAI GPT
- Support for Playwright and Cypress
- Azure DevOps integration
- Export generated scripts to files


## License

This project was created for educational purposes as part of an AI Project Prototype assignment.

