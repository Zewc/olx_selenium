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
        'https://www.olx.ua/d/uk/moda-i-stil/muzhskaya-obuv/q-%D0%B1%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%96-%D0%BA%D1%80%D0%BE%D1%81%D1%96%D0%B2%D0%BA%D0%B8/?page=2')
    print(1)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    print(2)
    close_popup_window = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[3]/div[3]/button"))).click()
    next_page = True
    while next_page == True:
        print(3)
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/form/div[5]/div/div[2]")))
        print(4)
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        print(5)
        block = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/form/div[5]/div/div[2]")
        print(6)
        elements = block.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        for element in elements:
            print(element.text)
            print(element.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        try:
            # Не переходить на 7 сторінку
            # 'https://www.olx.ua/uk/moda-i-stil/muzhskaya-obuv/q-%D0%B1%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%96-%D0%BA%D1%80%D0%BE%D1%81%D1%96%D0%B2%D0%BA%D0%B8/?page=6'

            next_page_btn = WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/a"))).click()
            print('button pressed')
        except Exception as ex:
            next_page = False

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
