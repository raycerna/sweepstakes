# Automated Sweepstakes Entry with Selenium

## This Python script automates the process of entering a sweepstakes on the GrabAGun website using the Selenium web automation framework. It fills out the sweepstakes entry form with user-provided information and schedules the entry to run at specified intervals.

### Requirements

- Python 3.x
- Selenium library
- Chrome WebDriver

# Setup
1. Install Python: If you don't already have Python installed, you can download it from the official Python website: https://www.python.org/downloads/

2. Install Selenium: You can install the Selenium library using pip, the Python package manager, with the following command:
*pip install selenium*

3. Download Chrome WebDriver: To use Selenium with Chrome, you need to download the Chrome WebDriver executable compatible with your Chrome browser version. You can download it from the official ChromeDriver website: https://sites.google.com/chromium.org/driver/. Make sure to place the Chrome WebDriver executable in your system's PATH or specify its location in the script.

# Usage
1. Open the script file (prepare.py) in a text editor.

2. Modify the script with your own information. Replace the example user information in the fill_grabagun_sweepstakes_form function with your own:
*fill_grabagun_sweepstakes_form("Your First Name", "Your Last Name", "your.email@example.com", "555-555-5555", "Your Address", "Your City", "Your State", "Your Zip Code")*

3. Schedule the function to run at specific intervals using the schedule library. You can adjust the frequency by changing the interval (in hours) in the following line:
*schedule.every(6).hours.do(fill_grabagun_sweepstakes_form, "Your First Name", "Your Last Name", "your.email@example.com", "555-555-5555", "Your Address", "Your City", "Your State", "Your Zip Code")*
Make sure to replace the example user information with your own.

4. Save the script.

5. Open Terminal or a command prompt and navigate to the directory where the script is located.

6. Run the script using the following command:
*python sweepstakes_entry.py*
The script will start filling out the form and submitting it at the specified intervals.

# **Disclaimer**
Please use this script responsibly and in accordance with the terms and conditions of the website you are interacting with. Automated interactions with websites may be subject to legal restrictions and should only be used for legitimate and ethical purposes.