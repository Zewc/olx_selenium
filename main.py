import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from data import write_data
import json

url = 'https://www.olx.ua/d/uk/moda-i-stil/muzhskaya-obuv/q-%D0%B1%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%96-%D0%BA%D1%80%D0%BE%D1%81%D1%96%D0%B2%D0%BA%D0%B8/?page='

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enable', False)
option.set_preference('dom.webnotifications.enable', False)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=option)
data = []
try:
    driver.maximize_window()
    driver.get(url)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    # close cookie access window
    close_popup_window = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[3]/div[3]/button"))).click()


    while WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-testid="pagination-forward"]'))):
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-cy="l-card"]')))
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        elements = driver.find_elements(By.XPATH, '//div[@data-cy="l-card"]')
        for element in elements:
            data.append(
                {
                    'name': element.find_element(By.TAG_NAME, 'h6').text,
                    'price': element.find_element(By.XPATH, '//p[@data-testid="ad-price"]').text,
                    'location-data': element.find_element(By.XPATH, '//p[@data-testid="location-date"]').text,
                    'link': element.find_element(By.TAG_NAME, 'a').get_attribute('href')
                }
            )

            # press the button to next page
        next_page_btn = WebDriverWait(driver, 40).until(EC.visibility_of_element_located(
            (By.XPATH, '//a[@data-testid="pagination-forward"]'))).click()

        write_data(data)


except Exception as ex:
    write_data(data)
    print(ex)

finally:
    driver.close()
    driver.quit()



# Message:
# Stacktrace:
# RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
# WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:180:5
# NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:392:5
# element.find/</<@chrome://remote/content/marionette/element.sys.mjs:134:16
