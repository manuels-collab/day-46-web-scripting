from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
#total_num_of_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount > ul > li:nth-child(2) > a:nth-child(1)')
#total_num_of_articles.click()

alL_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#alL_portals.click()

search_button = driver.find_element(By.LINK_TEXT, value="Search")
search_button.click()
search_field = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search_field.send_keys("Python", Keys.ENTER)