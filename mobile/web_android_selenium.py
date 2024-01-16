from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.common import AppiumOptions
import time

APPIUM = 'http://localhost:4723'

options = AppiumOptions()
options.set_capability("appium:platformName", "Android")
options.set_capability("appium:automationName", "UiAutomator2")
options.set_capability("appium:deviceName", "Android Emulator")
options.set_capability("appium:browserName", "Chrome")

# Iniciar appium server con el siguiente comando -> appium --allow-insecure=chromedriver_autodownload

# Initialize the driver
driver = webdriver.Remote(command_executor=APPIUM, options=options)

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