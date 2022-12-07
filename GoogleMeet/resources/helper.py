import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from time import sleep

wait = '-1'
meeting_code='-1'

def start_session(DEVICE):
    try:
        # Read the devices.json file and convert it into a Python object
        with open('GoogleMeet/resources/devices.json') as f:
            device_list = json.load(f)

        # Set the desired device name
        device = device_list[DEVICE]

        # Set up desired capabilities for the Appium driver using the specified device
        desired_caps = {
            "deviceName": device["deviceName"],
            "udid": device["udid"],
            "automationName": device["automationName"],
            "platformName": device["platformName"],
            "appPackage": device["appPackage"],
            "appActivity": device["appActivity"],
            "appium_url": device["appium_url"],
            "phone_number": device["phone_number"],
            "headspin:controlLock": "true"
        }
        
        # Create the Appium driver
        driver = webdriver.Remote(desired_caps['appium_url'], desired_caps)
        wait = WebDriverWait(driver, 10)

        # Open the Google Meet app
        driver.launch_app()

        return driver
    except Exception as e:
            # Return a string with the error message
            print( "Error starting driver: " + str(e))
            driver.quit()

def navigate_to_meet_app():
    try:
        # Find Google Meet app in app list and launch
        driver.find_element(by=AppiumBy.ID, value="com.android.settings:id/search_bar").click()
        searchbox = driver.find_element(by=AppiumBy.ID, value="com.google.android.settings.intelligence:id/open_search_view_edit_text")
        searchbox.send_keys("Meet")
        
        driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
        driver.find_element(by=AppiumBy.ID, value="com.android.settings:id/button1").click()

       
    except Exception as e:
        # Return a string with the error message
        print( "Error navigating to Meet App: " + str(e))
        driver.quit()


def start_meet_session():
    try:
        # Use Coords to click New Meeting button
        click_new_meeting_button = ActionChains(driver)
        click_new_meeting_button.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        click_new_meeting_button.w3c_actions.pointer_action.move_to_location(1184, 2803)
        click_new_meeting_button.w3c_actions.pointer_action.pointer_down()
        click_new_meeting_button.w3c_actions.pointer_action.pause(0.1)
        click_new_meeting_button.w3c_actions.pointer_action.release()
        click_new_meeting_button.perform()


        # Retreive meeting code & Join
        meeting_code = driver.find_element(by=AppiumBy.ID, value="com.google.android.apps.tachyon:id/meeting_link_copy_text").get_attribute('text')
        print(meeting_code)        
        driver.find_element(by=AppiumBy.ID, value="com.google.android.apps.tachyon:id/join_meeting_chip").click()
        driver.find_element(by=AppiumBy.ID, value="com.google.android.apps.tachyon:id/join_button_bottomsheet").click()


        sleep(60)
        # Return the Appium driver
        return driver
    except Exception as e:
        # Return a string with the error message
        print( "Error starting Meet session: " + str(e))
        driver.quit()




driver = start_session('pixel4xl_2')
navigate_to_meet_app()
start_meet_session()
