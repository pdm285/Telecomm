import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import resources.helper
from os import path
import os

# email = pmuller.earl@headspin.io
# password = teleworldpassword1




os.environ["HS_TOKEN"] = 'd20f04e28a0e436f9899c7aed2f92b82'
TOKEN = os.environ.get("HS_TOKEN")
ENDPOINT = "https://teleworld-api.headspin.io"



caps = {
    "deviceName": "SM-G998U1",
    "udid": "R5CR7165CTZ",
    "automationName": "uiautomator2",
    "appPackage": "com.android.settings",
    "platformName": "android",
    "appActivity": "com.android.settings.Settings"
}


hub_url=f"https://teleworld-us-cha-0.headspin.io:7022/v0/{TOKEN}/wd/hub"





caps["headspin:controlLock"]="true"
# caps["headspin:capture"]="true"
driver = webdriver.Remote(hub_url, caps)
wait = WebDriverWait(driver, 15)


try:
    # Create the Appium driver
    session_id = driver.session_id
    #Find & Open COD from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("Call of Duty")
    resources.helper.tap(driver,479,686)
    
    driver.find_element(MobileBy.ID,'com.android.settings:id/button1').click()


    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.google.android.gms:id/account_display_name'))).click()
    


    time.sleep(15)

    #Click [X] in pop up menu
    for i in range(3):
        resources.helper.tap(driver,1760,194)
        resources.helper.tap(driver,1780,164)
        resources.helper.tap(driver,1751,166)


    #Tap Multiplayer
    resources.helper.tap(driver,2022,484)


    ## REQUIRES USER INPUT
    for i in range(30):
        print('need user input')
        time.sleep(1)

    for i in range (15):
        resources.helper.move_forward(driver)
        resources.helper.move_forward(driver)
        resources.helper.move_forward(driver)
        resources.helper.move_forward(driver)
        resources.helper.move_forward(driver)
        resources.helper.move_forward(driver)
        resources.helper.look_left(driver)
        resources.helper.move_forward(driver)
        resources.helper.look_right(driver)
        resources.helper.look_right(driver)
        resources.helper.look_right(driver)
        resources.helper.move_forward(driver)
        time.sleep(1)







except Exception as e:
    print(e)

finally:
    driver.terminate_app("com.activision.callofduty.shooter")
    driver.quit