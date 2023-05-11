import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path
import os
import resources.helper

os.environ["HS_TOKEN"] = ''
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
# caps["headspin:capture"]="true"




try:
    # Create the Appium driver
    driver = webdriver.Remote('https://teleworld-us-cha-0.headspin.io:7022/v0/{TOKEN}/wd/hub', caps)
    driver.orientation = "PORTRAIT"
    wait = WebDriverWait(driver, 15)
    session_id = driver.session_id

    #Find & Open Zoom from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("Zoom app")
    resources.helper.tap(driver,255,1037)
    resources.helper.tap(driver,194,2146)


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

    resources.helper.tap(driver,281, 2136)


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