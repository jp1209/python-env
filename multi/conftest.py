import pytest
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from views.home_view import HomeView
from views.echo_views import EchoView

CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR,'TheApp.apk')
IOS_APP = ""
APPIUM = 'http://localhost:4700'

ANDROID_CAPS = dict(
    platformName='Android',
    automationName='UiAutomator2',
    deviceName='emulator-5554',
    deviceUDID='emulator-5554',
    udid='emulator-5554',
    app = ANDROID_APP,
    wdaLocalPort=8100,
    systemPort= 8200
    )

IOS_CAPS = dict(
    platformName='Android',
    automationName='UiAutomator2',
   # deviceName='emulator-5554',
   # deviceUDID="emulator-5554",
    udid='emulator-5556',
    app = ANDROID_APP,
    wdaLocalPort=8100,
    systemPort= 8200
    )

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')
    
@pytest.fixture
def platform(request):    
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios','android']:
        raise ValueError('--platform must be ios or android')
    return plat
    

@pytest.fixture
def driver(platform):

    caps = IOS_CAPS if platform == "android" else ANDROID_CAPS ###CORREGIR
    
    capabilities_options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(command_executor=APPIUM, options=capabilities_options)
    driver._platform = platform
    yield driver
    driver.quit()
    
@pytest.fixture
def home(driver):
    return HomeView.instance(driver)