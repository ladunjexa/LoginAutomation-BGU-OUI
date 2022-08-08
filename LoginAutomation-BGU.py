#================================================================================
#   ||          ------------------------------------------------            ||
#   ||         Login automation using Selenium WebDriver (chrome)           ||
#   ||         Adapted to the Ben-Gurion University (BGU) website		    ||
#   ||         @requirements: chromedriver, selenium, python                ||
#================================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

WEBSEITE_URL = "https://moodle.bgu.ac.il/moodle/local/mydashboard/" # website login URL
PATH_FOR_DRIVER = "C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe" # chromedriver.exe PATH

# Note: Student details, replace the following variables with your login information
USER_NAME = "USERNAME"
PASSWORD = "PASSWORD"

# Setting up the driver & canceling 'chrome controlled by automated-software'
chromeopt = webdriver.ChromeOptions()
chromeopt.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(executable_path=PATH_FOR_DRIVER, options=chromeopt)

driver.get(WEBSEITE_URL) # Open 'WEBSITE_URL' (at this case: OUOI Login page)

# Get desirable elements of student details & sending the appropriate keys (lines 25-27)
    # To use for another site, the id/class-names can be collected by using DevTools in the browser (F12).
        # Tap on inspect selector and select the required input elements for log-in, it'll show you the associated code
        # within the associated code/preview-inspector collect the relevant ids/class-names.
element = driver.find_element(By.ID, 'login_username') 
element.send_keys(USER_NAME)

element = driver.find_element(By.ID, 'login_password')
element.send_keys(PASSWORD)

element.send_keys(Keys.ENTER) # Press enter to log-in

while True:
    sleep(1) # stop Selenium from closing the browser
