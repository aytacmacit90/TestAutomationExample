from selenium import webdriver
import time

driver = webdriver.Chrome("C:\chromedriver.exe")
# driver =webdriver.Firefox()
# driver= webdriver.Ie()

driver.set_page_load_timeout(10)
driver.get("https://www.nesine.com")
driver.find_element_by_id("txtUsername").send_keys("aytac.macit@gmail.com")
driver.find_element_by_id("realpass").send_keys("*******")
driver.find_element_by_link_text("GİRİŞ").click()
time.sleep(4)
driver.quit()
