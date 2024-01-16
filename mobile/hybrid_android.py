import time
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='Android Emulator',
    app = APP
)

class webview_active(object): #wait.until(webview_active())
    def __call__(self, driver):
        for context in driver.contexts:
            if context != 'NATIVE_APP':
                driver.switch_to.context(context)
                return True
        return False


capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=APPIUM, options=capabilities_options)

try:
    wait = WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(
        (By.ACCESSIBILITY_ID ,'Webview Demo')
        )).click()
    
    wait.until(EC.presence_of_element_located(
        (By.XPATH,'//android.widget.EditText[@content-desc="urlInput"]'),  # parent element
    )).send_keys('https://appiumpro.com')
    
    

    driver.find_element(By.ACCESSIBILITY_ID, 'navigateBtn').click()
    wait.until(webview_active())

    print(driver.current_url)
    print(driver.title)
finally:
    driver.quit()