from selenium import webdriver
from os import system
import time

#Precio del Bitcoin con Web Scraping (Python y Selenium)

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://cuantoestaeldolar.pe/")

CompraSunat = driver.find_element_by_xpath('/html/body/div[3]/section/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]')
VentaSunat = driver.find_element_by_xpath('/html/body/div[3]/section/div[1]/div[3]/div/div[1]/div/div/div[2]/div[3]')
CompraParalelo = driver.find_element_by_xpath('/html/body/div[3]/section/div[1]/div[3]/div/div[1]/div/div/div[3]/div[2]')
VentaParalelo = driver.find_element_by_xpath('/html/body/div[3]/section/div[1]/div[3]/div/div[1]/div/div/div[3]/div[3]')
system("cls")
print('Sunat -> Compra:'+CompraSunat.text + ' Venta: '+VentaSunat.text)
print('Paralelo -> Compra: '+CompraParalelo.text+' Venta: '+VentaParalelo.text)

driver.quit()