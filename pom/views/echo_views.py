from selenium.webdriver.common.by import By
from views.base_views import BaseView
from selenium.common.exceptions import TimeoutException

class EchoView(BaseView):
    
    MESSAGE_INPUT =  (By.XPATH,'//*[@content-desc="messageInput"]')
    SAVE_BTN = (By.XPATH,'//*[@content-desc="messageSaveBtn"]')
    MESSAGE_LBL = (By.XPATH,'//*[@content-desc="Hello"]')
    
    
    def save_message(self,message):
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        self.find_for(self.SAVE_BTN).click()
        
    def read_message(self):
        try:
            return  self.wait_for(self.MESSAGE_LBL).text
        except TimeoutException:
            return None

    
    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView(self.driver)

        
    
    

    