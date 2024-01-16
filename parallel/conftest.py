import pytest
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from views.home_view import HomeView
from views.echo_views import EchoView

#DONE 1: define and prepare our test environments
#DONE 2: update conftest to allow *sets* of environments and not just one
#DONE 3: figure out which pytest worker is asking for a driver
#DONE 4: update driver a fixture to parameterize server and caps based worker id
#TODO 5: ensure that we don't try to run more parallel tests than we should

CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR,'TheApp.apk')
IOS_APP = ""
APPIUMS = ['http://localhost:4700', 'http://localhost:4701']

ANDROID_CAPS = [dict(
    platformName='Android',
    automationName='UiAutomator2',
    udid='emulator-5554',
    app = ANDROID_APP,
    wdaLocalPort=8100,
    systemPort= 8200
    ),dict(
    platformName='Android',
    automationName='UiAutomator2',
    udid='emulator-5556',
    app = ANDROID_APP,
    wdaLocalPort=8101,
    systemPort= 8201 
    )]

IOS_CAPS = [dict(
    platformName='Android',
    automationName='UiAutomator2',
    udid='emulator-5554',
    app = ANDROID_APP,
    wdaLocalPort=8100,
    systemPort= 8200
    ),dict(
    platformName='Android',
    automationName='UiAutomator2',
    udid='emulator-5556',
    app = ANDROID_APP,
    wdaLocalPort=8101,
    systemPort= 8201
    )]

def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')
    

@pytest.fixture
def worker_num(worker_id):
    #'master', 'gw1','gw2',...
    if worker_id == 'master':
        worker_id = 'gw0'
    return int(worker_id[2:])

@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise ValueError("Too many workers for Appium server")
    return APPIUMS[worker_num]

@pytest.fixture
def caps(platform, worker_num):
    cap_sets = IOS_CAPS if platform == 'ios' else ANDROID_CAPS
    if worker_num >= len(cap_sets):
        raise ValueError("Too many worker for the num of caps sets")
    return cap_sets[worker_num]

@pytest.fixture
def platform(request):    
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios','android']:
        raise ValueError('--platform must be ios or android')
    return plat
    

@pytest.fixture
def driver(server,caps, platform):
    capabilities_options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(command_executor=server, options=capabilities_options)
    driver._platform = platform
    yield driver
    driver.quit()
    
@pytest.fixture
def home(driver):
    return HomeView.instance(driver)