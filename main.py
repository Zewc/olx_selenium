from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enable', False)
option.set_preference('dom.webnotifications.enable', False)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=option)

try:
    driver.maximize_window()
    driver.get('https://www.olx.ua/d/uk/moda-i-stil/muzhskaya-obuv/q-%D0%B1%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%96-%D0%BA%D1%80%D0%BE%D1%81%D1%96%D0%B2%D0%BA%D0%B8/?currency=UAH&page=1')

    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    close_popup_window = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "css-1l30vq6"))).click()

    next_page = True
    while next_page == True:

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "css-oukcj3")))
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        block = driver.find_element(By.CLASS_NAME, "css-oukcj3")
        elements = block.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        for element in elements:
            print(element.text)
            print(element.find_element(By.CLASS_NAME, "css-rc5s2u").get_attribute('href'))
            print('/////////////////////////////////////////////')
        try:

            next_page_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "a[data-testid='pagination-forward']"))).click()
        except Exception:
            next_page = False

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()


#проходить страницы через driver.get