# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:01:24 2020

@author: Татьяна
"""

from selenium import webdriver
import math
import time 
link = "http://suninjuly.github.io/find_xpath_form"
#link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    #link = browser.find_element_by_link_text("224592")
    #link.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("I")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("P")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("S")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("R")
    button = browser.find_element_by_xpath('//button[text("Submit")]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла