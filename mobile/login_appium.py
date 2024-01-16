import time
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
#APP = path.join(CUR_DIR, 'booking.apk')
APPIUM = 'http://localhost:4723'

capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    #platformVersion='13.0',
    deviceName='Android Emulator',
    #appPackage='com.android.settings',
    app = APP
)


capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

try:
    driver = webdriver.Remote(command_executor=APPIUM, options=capabilities_options)
    time.sleep(4)
    driver.quit()
    
except Exception as e:
    print(f"Error al iniciar el driver: {e}")
    # Imprime el stack trace completo para obtener más información detallada
    print(e)