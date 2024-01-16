from selenium.webdriver.common.by import By
from views.base_views import BaseView
from views.echo_views import EchoView

class HomeView(BaseView):
    
    ECHO_ITEM = (By.XPATH,'//*[@content-desc="Echo Box"]') 
          
    
    def nav_echo_box(self):
        self.wait_for(self.ECHO_ITEM).click()
        return EchoView.instance(self.driver)
        
   
    

    