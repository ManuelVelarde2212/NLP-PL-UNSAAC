from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd


# navegation options
options = webdriver.ChromeOptions()
options.add_argument('__disable-extensions')
options.add_argument('--incognito')

driver_path = 'chromedriver'
driver = webdriver.Chrome(driver_path, options=options)

# initilize nav
driver.get('https://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2016.nsf/Local%20Por%20Numero%20Inverso?OpenView')

data = []
previous_url = driver.current_url

while True:
  # using xpath for each row
  table = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[2]')
  # ignore the last row
  file_url_size = len(table.find_elements(By.TAG_NAME, 'tr'))-1
  for i in range(1, file_url_size):
    wait = WebDriverWait(driver, 5)
    wait = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr/td/table[2]')))
    table = driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td/table[2]')
    rows = table.find_elements_by_xpath('.//tr')
    url_clickable = [td for td in rows[i].find_elements_by_xpath('.//td/font/a')]
    url_clickable[0].click()

    num_file = WebDriverWait(driver, 5)
    num_file = num_file.until(ec.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table')))
    num_file = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/u[2]/font').text
    period = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/font').text
    legislature = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/font').text
    date = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/font').text
    proponent = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/font').text
    parliament = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td/font').text
    title = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[6]/td/font').text
    object_ = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[7]/td/font').text
    data.append([num_file, period, legislature, date, proponent, parliament, title, object_])
    driver.back()

  next_button = WebDriverWait(driver, 10)
  next_button = next_button.until(ec.element_to_be_clickable((By.XPATH, '/html/body/form/table/tbody/tr/td/table[1]/tbody/tr/td[3]/a')))
  next_button.click()
  current_url = driver.current_url
  if previous_url == current_url: break
  else: previous_url = current_url
  stop = False

# csv headers
header = ['Expediente', 'Período', 'Legislatura', 'Fecha', 'Proponente', 'Parlamento', 'Título', 'Objeto']

laws = pd.DataFrame(data, columns=header)
laws.to_csv('laws.csv', index=False, sep=';')

