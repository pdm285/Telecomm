import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path
import os
import sys
import json
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from resources import helper


# Load JSON data from the config.json file
with open('resources/config.json', 'r') as file:
    config_data = json.load(file)


# Extract the capabilities from the Devices dictionary
caps = config_data['Devices']

caps["headspin:capture"] = False
caps["headspin:capture.video"] = True

# Create driver
try:
    driver = webdriver.Remote(f"https://{config_data['URL']}{config_data['HS_TOKEN']}/wd/hub", caps)
except Exception as e:
    print("error starting driver.  Stacktrace:")
    print(f"{e}")
    sys.exit(-1)

wait = WebDriverWait(driver, 15)
driver.orientation = "PORTRAIT"
session_id = driver.session_id


try:
    #Find & Open COD from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("Call of Duty")
    time.sleep(1)
    helper.tap(driver,479,686)
    
    driver.find_element(MobileBy.ID,'com.android.settings:id/button1').click()



    # Wait 2 minutes to download resources
    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.google.android.gms:id/account_display_name'))).click()
    


    time.sleep(15)
    #Click [X] in pop up menu
    for i in range(3):
        helper.tap(driver,1760,194)
        helper.tap(driver,1780,164)
        helper.tap(driver,1751,166)


    #Tap Multiplayer
    helper.tap(driver,2022,484)


    ## REQUIRES USER INPUT
    for i in range(30):
        print('need user input')
        time.sleep(1)

    for i in range (15):
        helper.move_forward(driver)
        helper.move_forward(driver)
        helper.move_forward(driver)
        helper.move_forward(driver)
        helper.move_forward(driver)
        helper.move_forward(driver)
        helper.look_left(driver)
        helper.move_forward(driver)
        helper.look_right(driver)
        helper.look_right(driver)
        helper.look_right(driver)
        helper.move_forward(driver)
        time.sleep(1)







except Exception as e:
    print(e)

finally:
    driver.terminate_app("com.activision.callofduty.shooter")
    driver.quit