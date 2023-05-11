import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.extensions.action_helpers import PointerInput
from selenium.webdriver.common.actions import interaction
from os import path
import os
import json
import requests
import sys


os.environ["HS_TOKEN"] = 'd20f04e28a0e436f9899c7aed2f92b82'
TOKEN = os.environ.get("HS_TOKEN")
ENDPOINT = "https://teleworld-api.headspin.io"

userflow = "Play ABC Live Stream on YouTube"
description = "test"

caps = {
    "deviceName": "SM-G998U1",
    "udid": "R5CR7165CTZ",
    "automationName": "uiautomator2",
    "appPackage": "com.android.settings",
    "platformName": "android",
    "appActivity": "com.android.settings.Settings"
}

caps["headspin:controlLock"]="true"

# START PERFORMANCE CAPTURE
caps["headspin:capture"]="true"

def tap(driver,x,y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()



try:
    # Create the Appium driver
    driver = webdriver.Remote('https://teleworld-us-cha-0.headspin.io:7022/v0/d20f04e28a0e436f9899c7aed2f92b82/wd/hub', caps)
    driver.orientation = "PORTRAIT"
    wait = WebDriverWait(driver, 15)
    session_id = driver.session_id
    #Find & Open YT from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("YouTube")
    tap(driver,479,686)
    tap(driver,194,2146)

    #Find ABC Live cast
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Search'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.google.android.youtube:id/search_edit_text'))).send_keys("ABC Live")
    driver.press_keycode(66)
    time.sleep(2)


    # driver.find_element(MobileBy.ACCESSIBILITY_ID,'Latest from ABC News')
    tap(driver, 355, 527)

    tap(driver,514, 543)


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
    print('https://ui-dev.headspin.io/sessions/' + str(session_id) + '/waterfall')




