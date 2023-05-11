from time import sleep
from appium.webdriver.common.touch_action import TouchAction

def tap(driver, x, y):
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()



def move_forward(driver):
    action = TouchAction(driver)
    action.press(x=280, y=737)
    action.move_to(x=280, y=649)
    sleep(3)
    action.release()
    action.perform()



def look_right(driver):
    action = TouchAction(driver)
    action.press(x=1521, y=612)
    action.move_to(x=1728, y=623)
    action.release()
    action.perform()


def look_left(driver):
    action = TouchAction(driver)
    action.press(x=1697, y=571)
    action.move_to(x=1417, y=571)
    action.release()
    action.perform()
