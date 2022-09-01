from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

TARGET_URL = 'https://www.clima.com'

driver = webdriver.Chrome(
    os.getenv('WEBDRIVER_PATH', '/Users/alfredomedrano/Development/tools/chromedriver'))

driver.get(TARGET_URL)

mxBtn = driver.find_element(By.CSS_SELECTOR, '#page > main > div.section_clima_home > div:nth-child(1) > section:nth-child(1) > div > ul > li.m_list_countrys_mx > a')

mxBtn.click()

time.sleep(1)
searchInput = driver.find_element(By.CSS_SELECTOR, '#term')
searchInput.send_keys('Querétaro')
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
stateTrigger = driver.find_element(By.CSS_SELECTOR, '#search > form > label > button')


time.sleep(1)

firstResult = driver.find_element(By.CSS_SELECTOR, '#page > main > div.section_search-results > div > section.block_thirds_left > section > div > ul > li:nth-child(1) > a')

firstResult.click()

time.sleep(1)
driver.execute_script("window.scrollTo(0, 1000);")
hoursTab = driver.find_element(By.CSS_SELECTOR, '#cityTable > div > article > section > ul > li:nth-child(2) > h2 > a')

hoursTab.click()
driver.execute_script("window.scrollTo(0, 1000);")

time.sleep(5)

#table = driver.find_element(By.CSS_SELECTOR, '#main > div.-t-xs-6.section_city > div > section.block_full.lazyloadcontent.row_box.row_number_5 > div > div:nth-child(2)')
##items = table.find_elements(By.XPATH, './/*')
items = driver.find_elements(By.CSS_SELECTOR, '#main > div.-t-xs-6.section_city > div > section.block_full.lazyloadcontent.row_box.row_number_5 > div > div:nth-child(2) > div')

print(len(items))

for item in items:
    div_class = item.get_attribute('class')
    if div_class != 'm_table_weather_hour_detail_header':
        hour = item.find_element(By.CSS_SELECTOR, 'div.m_table_weather_hour_detail_hours')
        weather = item.find_element(By.CSS_SELECTOR, 'div.m_table_weather_hour_detail_pred > span')
        print(hour.text, weather.text)