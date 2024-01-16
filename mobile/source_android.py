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
        (By.ACCESSIBILITY_ID ,'Login Screen')
        ))
    print(driver.page_source)

    # Guardar datos en un txt 
    #with open('pagina.txt', 'w',encoding="utf-8") as f:
    #    f.write(f'{driver.page_source}')
    
finally:
    driver.quit()