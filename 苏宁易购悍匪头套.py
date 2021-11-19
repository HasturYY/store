import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
driver.find_element_by_id("searchKeywords").send_keys("悍匪头套")
driver.find_element_by_id("searchSubmit").click()
driver.find_element_by_xpath('//*[@id="ssdsn_search_pro_baoguang-1-0-1_1_02:0070879179_12338873733"]/img').click()
# 获取窗口句柄
date = driver.window_handles
driver.switch_to.window(date[1])
driver.find_element_by_xpath('//*[@id="J-TZM"]/dl[1]/dd/ul/li[6]/a/span').click()
driver.find_element_by_xpath('//*[@id="buycount"]/dd/a[2]').click()
driver.find_element_by_id("addCart").click()
time.sleep(3)
driver.quit()






