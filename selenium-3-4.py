from selenium import webdriver
import time

chromedriver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chromedriver)


browser.get('https://www.baidu.com')
input_en = browser.find_element_by_id('kw')
input_en.send_keys('selenium python 教程')
time.sleep(2)
btn_en = browser.find_element_by_id('su')
btn_en.click()
time.sleep(10)
browser.close()
# 一堆的报错  然后是解决了一个问题  就解决了错误的问题 哈哈哈




