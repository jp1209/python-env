import pytest
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from views.home_view import HomeView
from views.echo_views import EchoView

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

@pytest.fixture
def driver():
    capabilities = dict(
        platformName='Android',
        automationName='UiAutomator2',
        deviceName='Android Emulator',
        app = APP
    )

    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(command_executor=APPIUM, options=capabilities_options)
    yield driver
    driver.quit()
    
@pytest.fixture
def home(driver):
    return HomeView(driver)