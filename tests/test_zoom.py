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


# Set the session ID from the provided parameter
config_data = json.loads(sys.argv[1])

# Create driver
try:
   driver = webdriver.Remote(f"https://{config_data['URL']}{config_data['HS_TOKEN']}/wd/hub", config_data['Devices'])
except Exception as e:
    print("error starting driver.  Stacktrace:")
    print("{e}")
    sys.exit(-1)


try:
    # Create the Appium driver
    driver.orientation = "PORTRAIT"
    wait = WebDriverWait(driver, 15)
    session_id = driver.session_id

    #Find & Open Zoom from settings app
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search settings"))).click()
    search_text = driver.find_element(by=MobileBy.ID, value="com.android.settings.intelligence:id/search_src_text").send_keys("Zoom app")
    time.sleep(1)
    helper.tap(driver,384, 1059)
    driver.find_element(MobileBy.ID,'com.android.settings:id/button1').click()


    #Join meeting
    try:
        wait.until(EC.presence_of_element_located((MobileBy.ID,"us.zoom.videomeetings:id/rooted_warning_dialog_continue_btn"))).click()
    except:
        print('rootbutton not found')

    wait.until(EC.presence_of_element_located((MobileBy.ID,"us.zoom.videomeetings:id/btnJoinConf"))).click()
    conference = driver.find_element(by=MobileBy.ID, value="us.zoom.videomeetings:id/edtConfNumber")
    conference.send_keys("5578624591")
    join = driver.find_element(by=MobileBy.ID, value="us.zoom.videomeetings:id/btnJoin")
    join.click()
    time.sleep(1)

    driver.find_element(by=MobileBy.ID, value="us.zoom.videomeetings:id/btnJoinWithVideo").click()




    print('awaiting to be let into room')
    time.sleep(5)
    wait.until(EC.presence_of_element_located((MobileBy.ID,"us.zoom.videomeetings:id/txtCallViaVoIP"))).click()




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