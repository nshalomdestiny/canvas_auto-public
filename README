# Canvas Automation Script Documentation

## Overview
This Python script is designed to automate the login process and retrieve assignment/announcement information from a Canvas website for PGCPS students using Selenium WebDriver. It interacts with specific elements on the Canvas website to log in and gather today's assignments or announcements.

## Requirements
- Python 3.x
- Selenium WebDriver for Python
- Chrome WebDriver
- YAML library for Python

## Usage
1. Ensure all necessary dependencies are installed.
2. Update the `loginDetails.yml` file with valid Canvas login credentials.
3. Update the URL with your Schools/County's Canvas URL
4. Run the script.

## File Structure
- `canvas_auto.py`: Main Python script.
- `loginDetails.yml`: YAML file containing login credentials (username and password) for Canvas.
- `chromedriver.exe` : WebDriver executable for communication between Selenium and Chrome.

## Script Structure
### Libraries Used
- `webdriver` from Selenium: For web automation.
- `yaml`: For reading login credentials from a YAML file.

### Functions
1. `login(url, usernameID, username, passwordId, password, submit)`: Performs the login action by opening the Canvas website, entering the provided username and password, and submitting the form.

2. `assignment()`: Searches for today's assignments or announcements on the Canvas planner and retrieves relevant information.

### Main Execution
- Reads login credentials from `loginDetails.yml`.
- Calls the `login()` function to log in to the Canvas website.
- Calls the `assignment()` function to retrieve today's assignments or announcements.

## Important Notes
- Ensure the `Chrome WebDriver` is installed and its path is set in the system's environment variables.
- Regularly check and update the script's locators if there are changes on the Canvas website to avoid breaking the automation process.
- Store sensitive information securely and avoid sharing credentials in code repositories.

## Maintenance and Future Improvements
- Periodically review and update the script to handle changes in the Canvas website's structure.
- Implement error handling for edge cases and improve efficiency where possible.
- Consider implementing encryption for storing and handling sensitive data.

## ENJOY
- Now you can check Canvas with just a click of a button

