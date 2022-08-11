from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Chrome():
    def Chrome_launch(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/")
        driver.maximize_window()

        time.sleep(7)
        driver.close()

test_obj=Chrome()
test_obj.Chrome_launch()



