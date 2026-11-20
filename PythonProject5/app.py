import streamlit as st

st.set_page_config(page_title="QA Automation Assistant")

st.title("QA Automation Assistant")

st.write(
    "This prototype converts manual QA test cases into Selenium automation scripts."
)

test_case = st.text_area(
    "Enter a Manual Test Case",
    height=200,
    placeholder="Example: Verify user can login with valid credentials."
)

if st.button("Generate Automation Script"):

    if test_case:

        generated_script = f"""
# Generated Selenium Test Script

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Test Case Provided by User:
# {test_case}

# AI-Generated Test Steps

"""

        if "login" in test_case.lower():

            generated_script += """
driver.get("https://example.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("testuser")
password.send_keys("Password123")

driver.find_element(By.ID, "login").click()

assert "Dashboard" in driver.title
"""

        elif "password" in test_case.lower():

            generated_script += """
driver.get("https://example.com/forgot-password")

email = driver.find_element(By.ID, "email")
email.send_keys("user@test.com")

driver.find_element(By.ID, "submit").click()

assert "Reset Email Sent" in driver.page_source
"""

        else:

            generated_script += """
# Generic Selenium template

driver.get("https://example.com")

# Add generated test actions here

assert True
"""

        generated_script += """

driver.quit()
"""

        st.success("Automation script generated successfully!")

        st.subheader("Generated Selenium Script")

        st.code(generated_script, language="python")