import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")
timeout = time.time() + 60 * 5
for i in range(500):
    while True:
        cookie.click()
        if time.time()> timeout:
            clicker = driver.find_element(By.XPATH, value='//*[@id="product1"]/div[3]/div')
            clicker.click()