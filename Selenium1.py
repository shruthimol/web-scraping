from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://jobsbrij.com/")
print(driver.title)
search=driver.find_element_by_name("word")
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(10)

