
from time import sleep
import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def enroll_whatsapp(driver, number):
    try:
        wait = WebDriverWait(driver,10)
        driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/eula_accept").click()
        # el1.click()
        sleep(1)

        driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/registration_phone").send_keys(number)
        sleep(1)

        driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/registration_submit").click()
        sleep(2)

        driver.find_element(by=AppiumBy.ID, value="android:id/button1").click()
        sleep(10)

        driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/submit").click()
        sleep(2)

        driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(2)

        driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(2)

        driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/dont_restore").click()
        sleep(2)

        driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SKIP RESTORE").click()
        sleep(2)

        driver.find_element(by=AppiumBy.ID, value="com.whatsapp:id/register_name_accept").click()
        sleep(2)
        print("Device enrolled with #{}".format(number))
        driver.quit()
    except Exception as e:
        print("Error occured during enrollment: {error}!".format(e))
        driver.quit()