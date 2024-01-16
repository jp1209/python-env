import time
from appium import webdriver
from os import path
from appium.options.android import UiAutomator2Options
from appium.webdriver.extensions.android.activities import Activities



CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
#APP = path.join(CUR_DIR, 'booking.apk')
APPIUM = 'http://localhost:4723'

capabilities = dict(
    platformName='Android',
    automationName='UiAutomator2',
    #platformVersion='13.0', #Solo si se quiere especificar
    deviceName='Android Emulator',
    app = APP 
)


capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=APPIUM, options=capabilities_options)


app = path.join(CUR_DIR, 'ApiDemos.apk')
app_id = "io.appium.android.apis";

app_act1 = ".graphics.TouchPaint"
app_act2 = ".text.Marquee"

try:   

    driver.install_app(app)
    activity_details = {'component': f'{app_id}/{app_act1}'}

    # Executing the custom Appium command
    driver.execute_script('mobile: startActivity', activity_details)
    time.sleep(2)
    activity_details = {'component': f'{app_id}/{app_act2}'}
    driver.execute_script('mobile: startActivity', activity_details)
    time.sleep(2)


    
finally:
    driver.quit()