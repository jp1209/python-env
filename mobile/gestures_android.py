import time
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton


CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
#APP = path.join(CUR_DIR, 'booking.apk')
APPIUM = 'http://localhost:4723'

capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    #platformVersion='13.0', #Solo si se quiere especificar
    deviceName='Android Emulator',
    app = APP
)


capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=APPIUM, options=capabilities_options)

try:
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID ,'List Demo')
        )).click()
        
    wait.until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID , 'Altocumulus')
    ))

    scroll = ActionBuilder(driver)
    finger = scroll.add_pointer_input(POINTER_TOUCH, "finger")
    finger.create_pointer_move(duration = 0, x = 100, y= 500)
    finger.create_pointer_down()
    finger.create_pointer_move(duration = 250, x = 0, y = -500, origin ="pointer")
    finger.create_pointer_up(0)
    scroll.perform()

    time.sleep(4)

    driver.find_element(By.ACCESSIBILITY_ID, 'Stratocumulus')
    
finally:
    driver.quit()