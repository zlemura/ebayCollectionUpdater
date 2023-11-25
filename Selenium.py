from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup

def initialise_webdriver():
    driver = webdriver.Edge('./msedgedriver.exe')
    return driver

def close_webdriver(driver):
    driver.close()

def open_collectible_page(driver, collectibleId):
    url = "https://www.ebay.com/collection/collectible?notionalTypeId=Soccer&period=1Y&collectibleId=" + str(collectibleId)
    driver.get(url)
    return driver

def click_collectible_edit_button(driver, collectibleId):
    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ebay-button-with-tourtip.icon-btn--edit"))
        ) #Retry every 10 seconds until element found.
    finally:
        edit_button_div = driver.find_element(By.CLASS_NAME, "ebay-button-with-tourtip.icon-btn--edit")

    edit_button = edit_button_div.find_element(By.CLASS_NAME, 'icon-btn')
    edit_button.click()