from selenium import webdriver
import time

visibility= False

driver = webdriver.Chrome("C:\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://www.nesine.com")
driver.find_element_by_id("txtUsername").send_keys("aytac.macit@gmail.com")
driver.find_element_by_id("realpass").send_keys("*******")
driver.find_element_by_link_text("GİRİŞ").click()
time.sleep(4)


driver.find_element_by_id("kupondas").click()
driver.refresh()
time.sleep(4)

driver.find_element_by_xpath("//div[@id='feedcontainer']/div[contains(@class,'feeditem')]").click()
time.sleep(4)

try:
    visibility=driver.find_element_by_xpath("//div[@class='feeds-detail']/div[contains(@class,'user-lock')]/a").is_displayed()
except:
    print("There is no such an element!!")
time.sleep(5)
if visibility==True:
    driver.find_element_by_xpath("//div[@class='feeds-detail']/div[contains(@class,'user-lock')]/a").click()
else:
    driver.find_element_by_xpath("//div[contains(@class,'iddaa-coupon-main')]/div[contains(@class,'coupon-footer')]/div[contains(@class,'playable')]/div[@class='right-side']/a").click()

time.sleep(6)

driver.find_element_by_xpath("//div[@class='couponButtons']/div[contains(@title,'HEMEN OYNA')]").click()

time.sleep(6)

driver.find_element_by_xpath("//div[@class='couponButtons']/div[contains(@title,'Onayla')]").click()


