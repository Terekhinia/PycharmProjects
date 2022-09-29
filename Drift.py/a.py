

from selenium import webdriver

drv = webdriver.Chrome('chromedriver.exe')
drv.get('https://www.google.com')
drv.close()