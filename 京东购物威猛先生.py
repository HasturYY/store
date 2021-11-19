
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.jd.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_c']").send_keys("威猛先生")
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@href="//cart.jd.com/gate.action?pid=8622230&pcount=1&ptype=1"]').click()
driver.quit()

















