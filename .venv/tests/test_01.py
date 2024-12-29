from selenium import webdriver
import time
from pages.search import mapleLandSearchPage

def test_01(browser):
    search_page = mapleLandSearchPage(browser)

    search_page.load()
    time.sleep(5)