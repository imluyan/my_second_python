# -*- coding: utf-8 -*-
from selenium import webdriver
import time

url = 'https://www.mql5.com/zh/trading'
driver = webdriver.Safari()
driver.get(url)
time.sleep(10)
driver.switch_to.frame('webTerminalHost')
while True:
    body_element = driver.find_element_by_tag_name('tbody')
    forex_element_lst = body_element.find_elements_by_tag_name('tr')

    for forex_element in forex_element_lst:
        forex = forex_element.get_attribute('id')
        price_bid = forex_element.find_element_by_id('bid')
        price_ask = forex_element.find_element_by_id('ask')
        print(forex, price_bid.text, price_ask.text)
