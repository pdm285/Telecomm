from appium import webdriver
import json




SENDER = webdriver.Remote(SENDER['appium_url'],SENDER)
RECEIVER = webdriver.Remote(RECEIVER['appium_url'],RECEIVER)

SENDER.quit()
RECEIVER.quit()