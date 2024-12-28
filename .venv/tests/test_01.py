from selenium import webdriver
import time

def test_01(browser):
    url = "http://www.naver.com"
    #driver = webdriver.Chrome()
    browser.get(url)
    time.sleep(5)