# -*- coding: utf-8 -*-
import sqlite3
import ssl
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = 'https://www.mql5.com/zh/trading'
driver = webdriver.Safari()
driver.get(url)
driver.switch_to.frame('webTerminalHost')
try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'GBPUSD'))
    )
    money_element_lst = driver.find_elements_by_tag_name('tbody')
    for every in money_element_lst:
        print(every)

finally:
    driver.quit()
