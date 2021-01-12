# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:58:17 2020

@author: Татьяна
"""

from selenium import webdriver

#import math
import time
from selenium.webdriver.support.ui import Select
#browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
#browser = webdriver.Chrome()
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #n1 = browser.find_element_by_id("num1")#z = int(x) + int(y)
    n1 = browser.find_element_by_id("num1")
    n2 = browser.find_element_by_id("num2")

    x = n1.text
    y = n2.text
    z = int(x) + int(y)
    #z = str(z)
    #browser.find_element_by_id("dropdown").click()
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()