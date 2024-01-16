from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_echo_box(driver):
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
        