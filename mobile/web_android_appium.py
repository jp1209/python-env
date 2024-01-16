from appium import webdriver
from appium.webdriver.common.appiumby import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
import time


APPIUM = 'http://localhost:4723'

    # Initialize Appium Options
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "YourDeviceName"  # Replace with your device name
options.automation_name = "UiAutomator2"
options.app_package = "com.android.chrome"  # Chrome package on Android
options.app_activity = "com.google.android.apps.chrome.Main"  # Chrome app main activity
options.no_reset = True  # Prevent resetting app state before this session
# Initialize WebDriver
driver = webdriver.Remote(APPIUM, options=options)

try:
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/")
    element = driver.find_element(By.LINK_TEXT,"Form Authentication")
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT,'Form Authentication')
        ))
    
    form_auth_link.click()

    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#username")
        ))
    username.send_keys('tomsmith')

    password = driver.find_element(By.CSS_SELECTOR,"#password")
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()

    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, "Logout")
        )).click()
    
    flash = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')
    ))

    driver.save_screenshot('primerImagen.png') #Sino se coloca la ruta se guarda en la carpeta del proyecto

    assert 'logged out' in flash.text

finally:
    driver.quit() 