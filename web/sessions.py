from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
try:
    driver.get("https://the-internet.herokuapp.com/")
    #wait = WebDriverWait(driver, 10)
    
    element = driver.find_element(By.LINK_TEXT,"Form Authentication")

    els = driver.find_elements(By.TAG_NAME,'a')
    print(f'There were {len(els)} anchor elements')

    els = driver.find_elements(By.TAG_NAME,'foo')
    print(f'There were {len(els)} anchor elements')
    
    #wait.until(EC.element_to_be_clickable(element))

    #element.send_keys("Metallica")
finally:
    driver.quit()