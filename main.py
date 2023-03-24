from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fake_useragent import UserAgent
import time
import random

useragent = UserAgent()

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enable', False)
option.set_preference('dom.webnotifications.enable', False)

# option.set_preference("general.useragent.override", useragent.random)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=option)

try:
    driver.maximize_window()
    driver.get(
        'https://www.olx.ua/d/uk/moda-i-stil/muzhskaya-obuv/q-%D0%B1%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%96-%D0%BA%D1%80%D0%BE%D1%81%D1%96%D0%B2%D0%BA%D0%B8/?page=')
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    close_popup_window = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[3]/div[3]/button"))).click()
    time.sleep(10000)
    next_page = True
    while next_page == True:
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".css-oukcj3")))

        except:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.css-oukcj3:nth-child(4)")))

        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        block = driver.find_element(By.CSS_SELECTOR, ".css-oukcj3")
        elements = block.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        for element in elements:
            print(element.text)
            print(element.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        try:
            next_page_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".pagination-list > a:nth-child(7)"))).click()
            print('button pressed')
        except Exception as ex:
            next_page = False

except Exception as ex:
    print('- [Exception]: ')
    print(ex)
    time.sleep(1000)
finally:
    driver.close()
    driver.quit()


page_higher_10 = 'CSS SELECTOR - div.css-oukcj3:nth-child(4)'


