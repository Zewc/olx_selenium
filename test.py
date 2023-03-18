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
    driver.get(
        'https://www.olx.ua/d/uk/moda-i-stil/muzhskaya-obuv/q-%D0%B1%D0%B0%D1%81%D0%BA%D0%B5%D1%82%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%96-%D0%BA%D1%80%D0%BE%D1%81%D1%96%D0%B2%D0%BA%D0%B8/?page=2')

#     driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
#     close_popup_window = WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[10]/button"))).click()
#
#     html = driver.page_source
#     with open('page.html', 'w', encoding='utf-16') as file:
#         file.write(html)
#
# except Exception as ex:
#     print(ex)
#
# finally:
#     driver.close()
#     driver.quit()
#
#
#
# xpath1 = '/html/body/div/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/a'
# xpath4 = '/html/body/div/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/a[2]'
# xpath5 = '/html/body/div/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/a[2]'
# xpath6 = '/html/body/div/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/a[2]'
# xpath10 = '/html/body/div/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/a[2]'
# xpath7 = '/html/body/div/div[1]/div[2]/form/div[5]/div/section[1]/div/ul/a[2]'

except:
    pass