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

if(config_data['HS_TOKEN']==None):
    print("You must configure your api key in the resources/config.json file")
    exit(1)

# Extract the capabilities from the Devices dictionary
devices = config_data['Devices']
caps = {
    'deviceName': devices['deviceName'],
    'udid': devices['udid'],
    'automationName': devices['automationName'],
    'appPackage': devices['appPackage'],
    'platformName': devices['platformName'],
    'appActivity': devices['appActivity'],
}

# Access other values from the config_data dictionary
hs_token = config_data['HS_TOKEN']
hub_url = f"{devices['URL']}{hs_token}/wd/hub"



caps["headspin:controlLock"]="true"

# START PERFORMANCE CAPTURE
# caps["headspin:capture"]="true"




try:
    # Create the Appium driver
    driver = webdriver.Remote(hub_url, caps)
    wait = WebDriverWait(driver, 15)




    session_id = driver.session_id
    #Find & Open COD from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("Call of Duty")
    helper.tap(driver,479,686)
    
    driver.find_element(MobileBy.ID,'com.android.settings:id/button1').click()


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