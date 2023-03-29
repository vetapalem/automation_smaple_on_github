from selenium import webdriver as wb
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains 
from webdriver_manager.chrome import ChromeDriverManager as ch
import time as tt
from code_test_pro import progress_bar as pp
class mike:  
    __obj1=pp()
    def link(li):
        li.driv=wb.Chrome(service=Service(executable_path=ch().install()))
        mike.__obj1.bar()
        li.driv.get(url=r'https://vetapalem.github.io/css-position/position.html')
        mike.__obj1.bar()
        li.driv.set_page_load_timeout(25)
        li.driv.maximize_window()
        tt.sleep(5)
        print(li.driv.page_source)
        li.driv.quit()


r=mike()
r.link()
