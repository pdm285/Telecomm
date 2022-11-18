from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json
from time import sleep


device = {}

try:
    device = json.loads('{"__type__": "device","deviceName": "Pixel 4 XL", "udid": "99151FFBA003EP", "automationName": "UiAutomator2", "appPackage": "com.android.settings", "platformName": "Android", "appActivity": "com.android.settings.Settings", "app":"", "appium_url":"https://dev-us-mv-0.headspin.io:3012/v0/6a4378b310dc4d95b712f5da9ef7accb/wd/hub"}') 
except: 
    print("Failed to load")

try:
    driver = webdriver.Remote(device['appium_url'],device)
    sleep(1)
    driver.press_keycode(4)
    driver.press_keycode(4)
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Call of Duty').click()
    sleep(10)
    driver.quit()




except Exception as e:
    print("Error occurred: {error}!!!!!".format(e))
    driver.quit()


