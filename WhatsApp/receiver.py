from time import sleep
import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import http.client



try:
    RECEIVER =  json.loads('{"__type__": "device", "deviceName": "Pixel 4 XL", "udid": "9A281FFBA003YA", "automationName": "uiautomator2", "appPackage": "com.whatsapp", "platformName": "Android", "appActivity": "com.whatsapp.Main", "appium_url":"https://dev-us-mv-0.headspin.io:3012/v0/6a4378b310dc4d95b712f5da9ef7accb/wd/hub"}')

    driver = webdriver.Remote(RECEIVER['appium_url'],RECEIVER)

    wait = WebDriverWait(driver,10)

    el1 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/eula_accept")
    el1.click()
    sleep(1)

    el2 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/registration_phone")
    el2.send_keys("6502857316")
    sleep(1)

    el3 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/registration_submit")
    el3.click()
    sleep(2)

    el4 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
    el4.click()
    sleep(6)

    el5 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/submit")
    el5.click()
    sleep(2)

    el6 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
    el6.click()
    sleep(2)

    el7 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button")
    el7.click()
    sleep(2)

    el8 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/dont_restore")
    el8.click()
    sleep(2)

    el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SKIP RESTORE")
    el9.click()
    sleep(2)

    el10 = driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/register_name_accept")
    el10.click()
    sleep(2)


    driver.quit()
except Exception as e:
    print("Error occured {error}".format(e))
    driver.quit()