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

driver = webdriver.Remote(hub_url, caps)



try:
    # Create the Appium driver
    wait = WebDriverWait(driver, 15)



    driver.orientation = "PORTRAIT"
    wait = WebDriverWait(driver, 15)
    session_id = driver.session_id
    #Find & Open YT from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("YouTube")
    helper.tap(driver,479,686)
    helper.tap(driver,194,2146)

    #Find ABC Live cast
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Search'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.google.android.youtube:id/search_edit_text'))).send_keys("ABC Live")
    driver.press_keycode(66)
    time.sleep(2)


    # driver.find_element(MobileBy.ACCESSIBILITY_ID,'Latest from ABC News')
    helper.tap(driver, 355, 527)

    helper.tap(driver,514, 543)


    time.sleep(2)
    driver.orientation = "LANDSCAPE"


    #
    # Timer 15 cycles of 60 seconds
    print("starting video")
    for i in range(0, 15):
        #sleep for 60 seconds
        time.sleep(60)
        print(f"{60*(i+1)} seconds passed")
        driver.find_element(MobileBy.ID,  'android:id/content')

except Exception as e:
    print(e)

finally:
    driver.terminate_app("com.google.android.youtube")
    driver.quit()
    # print('https://ui-dev.headspin.io/sessions/' + str(session_id) + '/waterfall')




