from appium import webdriver
import json
import pytest
import resources.helpers as helper



CALLER = json.loads('{"__type__": "device","deviceName": "Pixel 4 XL", "udid": "99151FFBA003EP", "automationName": "UiAutomator2", "appPackage": "com.whatsapp", "platformName": "Android", "appActivity": "com.whatsapp.Main", "app":"", "appium_url":"https://dev-us-mv-0.headspin.io:3012/v0/6a4378b310dc4d95b712f5da9ef7accb/wd/hub"}') 
CALL_DRIVER = webdriver.Remote(CALLER['appium_url'],CALLER)

RECEIVER =  json.loads('{"__type__": "device", "deviceName": "Pixel 4 XL", "udid": "9A281FFBA003YA", "automationName": "uiautomator2", "appPackage": "com.whatsapp", "platformName": "Android", "appActivity": "com.whatsapp.Main", "appium_url":"https://dev-us-mv-0.headspin.io:3012/v0/6a4378b310dc4d95b712f5da9ef7accb/wd/hub"}')
RECEIVER_DRIVER = webdriver.Remote(RECEIVER['appium_url'],RECEIVER)


helper.enroll_device(CALL_DRIVER)



SENDER.quit()
RECEIVER.quit()