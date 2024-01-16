from selenium import webdriver

caps = {
    "browserName": "Chrome"
}

options = webdriver.ChromeOptions()  # Cambia a FirefoxOptions si estás usando Firefox

for key, value in caps.items():
    options.set_capability(key, value)

driver = webdriver.Remote(
    command_executor='http://localhost:9515',
    options=options
)

driver.quit()