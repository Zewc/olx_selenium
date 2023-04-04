import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import json

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enable', False)
option.set_preference('dom.webnotifications.enable', False)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=option)

try:
    driver.maximize_window()
    driver.get(
        'https://www.olx.ua/d/uk/moda-i-stil/muzhskaya-obuv/q-%D0%B1%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%96-%D0%BA%D1%80%D0%BE%D1%81%D1%96%D0%B2%D0%BA%D0%B8/?page=')
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    # close cookie access window
    close_popup_window = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[3]/div[3]/button"))).click()

    data = []

    WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@data-cy="l-card"]')))
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    elements = driver.find_elements(By.XPATH, '//div[@data-cy="l-card"]')
    for element in elements:
        data.append(
            {
                'grade': element.find_element(By.XPATH, '//span[@title]').text
            }
        )

    with open('test.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)




except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
