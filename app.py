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
driver.implicitly_wait(10)
driver.get(url)

try:
    print(driver.page_source)
except:
    pass