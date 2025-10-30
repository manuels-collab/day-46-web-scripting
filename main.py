from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options =  webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.com/Apple-iPhone-Version-256GB-Titanium/dp/B0DPDJ3PJF/ref=sr_1_4?crid=2ZR6LSBEILT58&dib=eyJ2IjoiMSJ9.xGhoXX0mTwN0QSb81eIT4MjId1e58AWu9uoieNWT1IWpMymJ4EVMP5ngrmZKMFROYkH90zy63gx6C-GuH28ZcwTwcHFdKvjXDqIERJN9fm2XpNge_SHpz316zfcRbRbfG3qi9nCeA2VrkG7e4o4uTCSLsYL1Lg_9ohn0SvPtTjvfLAPvYfm3sxLDLCC8ZJsy7Skvl2yKuvHHSlU583pyuTWZwr0y14M7gUYVfEz9798.jKQMM-Y37NUQPPR2UWiG427-qNGJOBE5n_28dBZLYMo&dib_tag=se&keywords=iphone+16+pro+max&qid=1757112345&sprefix=iphon%2Caps%2C330&sr=8-4")
#driver.implicitly_wait(10)
#price_dollar = driver.find_element(By.XPATH, value='//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')
#print(f"The price is {price_dollar.text}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
events_time = driver.find_elements(By.CSS_SELECTOR, value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > time')
events_list = driver.find_elements(By.CSS_SELECTOR, value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a")
events = {}
for n in range(len(events_time)):
    events[n] = {
        "time": events_time[n].text,
        'name': events_list[n].text,
    }
print(events)


driver.quit()