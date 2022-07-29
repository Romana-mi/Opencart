from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class OpenCartDemo():
    def register(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")

        # Find Elements

        firstname = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
        lastname = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
        email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
        password = driver.find_element(By.CSS_SELECTOR, '#input-password')
        subscribe = driver.find_element(By.XPATH, '//*[@id="input-newsletter-no"]')
        checkbox = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/div/input')

        # agree_policy = driver.find_element(By.NAME, "agree")

        Continue = driver.find_element(By.CSS_SELECTOR, "#form-register > div > div > button")

        # Login Action
        firstname.clear()
        firstname.send_keys('Romana')

        lastname.clear()
        lastname.send_keys('akther')

        email.clear()
        email.send_keys('romanaakther8090@gmail.com')

        password.clear()
        password.send_keys('rom1234')

        # driver.find_element(By.NAME,"agree").click()

        Continue.click()
        time.sleep(8)
        driver.close()


test_obj = OpenCartDemo()
test_obj.register()
