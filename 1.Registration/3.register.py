from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Demo_Opencart():
    def register(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        driver.maximize_window()

        driver.find_element(By.ID,"input-firstname").send_keys("romana")
        time.sleep(2)
        driver.find_element(By.NAME,"lastname").send_keys("aktar")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#input-email").send_keys("rom@mail.com")
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="input-password"]').send_keys("rom123")
        time.sleep(2)
        driver.find_element(By.NAME,"newsletter").click()
        time.sleep(2)
        var1=driver.find_element(By.NAME,"newsletter").is_selected()
        print(var1)
        driver.find_element(By.NAME,"agree").click()
        time.sleep(2)
        var2 = driver.find_element(By.NAME, "agree").is_selected()
        print(var2)
        driver.find_element(By.CSS_SELECTOR,"#form-register > div > div > button").click()
        time.sleep(3)
        driver.close()



reg_obj = Demo_Opencart()
reg_obj.register()
