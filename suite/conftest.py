import pytest
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
#APP = path.join(CUR_DIR, 'booking.apk')
APPIUM = 'http://localhost:4723'

@pytest.fixture
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='UiAutomator2',
        #platformVersion='13.0', #Solo si se quiere especificar
        deviceName='Android Emulator',
        app = APP
    )

    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(command_executor=APPIUM, options=capabilities_options)
    yield driver
    driver.quit()