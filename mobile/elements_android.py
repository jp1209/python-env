import time
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        (By.ACCESSIBILITY_ID ,'Echo Box')
        )).click()
        
    wait.until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID ,'messageInput')
    )).send_keys('Hello')

    driver.find_element(By.ACCESSIBILITY_ID,'messageSaveBtn').click()
    
    write_text = 'Hello'
    saved_text = wait.until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID ,write_text))).text
    assert saved_text == 'Hello'

    driver.back()

    wait.until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID ,'Echo Box'))).click()
    
    saved_text = wait.until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID ,write_text))).text
    assert saved_text == 'Hello'
    time.sleep(4) 
    
finally:
    driver.quit()