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
    driver.orientation = "PORTRAIT"
    wait = WebDriverWait(driver, 15)
    session_id = driver.session_id

    #Find & Open Zoom from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("Zoom app")
    helper.tap(driver,384, 1059)
    driver.find_element(MobileBy.ID,'com.android.settings:id/button1').click()


    #Join meeting
    try:
        wait.until(EC.presence_of_element_located((MobileBy.ID,"us.zoom.videomeetings:id/rooted_warning_dialog_continue_btn"))).click()
    except:
        print('rootbutton not found')

    wait.until(EC.presence_of_element_located((MobileBy.ID,"us.zoom.videomeetings:id/btnJoinConf"))).click()
    conference = driver.find_element(by=MobileBy.ID, value="us.zoom.videomeetings:id/edtConfNumber")
    conference.send_keys("9751892899")
    join = driver.find_element(by=MobileBy.ID, value="us.zoom.videomeetings:id/btnJoin")
    join.click()
    time.sleep(1)
    passcode = driver.find_element(by=MobileBy.ID, value="us.zoom.videomeetings:id/edtPassword")
    passcode.send_keys("Cpe2PA")
    time.sleep(1)

    join = driver.find_element(by=MobileBy.ID, value="us.zoom.videomeetings:id/button1")
    join.click()
    


    wait.until(EC.presence_of_element_located((MobileBy.ID,"us.zoom.videomeetings:id/txtCallViaVoIP"))).click()

    helper.tap(driver,281, 2136)


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
    driver.terminate_app('us.zoom.videomeetings')
    driver.quit()