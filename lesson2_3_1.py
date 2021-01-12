# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:25:21 2021

@author: Татьяна
"""

from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    #browser.switch_to.window(new_window)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text 
    y = calc(x)
    input1=browser.find_element_by_id("answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()