import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
driver.maximize_window()
'''
b站登录需要手机验证所以无法进行登录，只能以游客的方式进行自动化操作
'''
time.sleep(4)
driver.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys("别录了")
driver.find_element_by_xpath('//*[@id="nav_searchform"]/div').click()
time.sleep(2)
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath('//*[@src="//i2.hdslb.com/bfs/archive/78c3861bb7deef91eb7ba2d2476f48a72ae491ea.jpg@320w_200h_1c.webp"]').click()
time.sleep(2)
windows = driver.window_handles
driver.switch_to.window(windows[2])
driver.find_element_by_xpath('//*[@id="arc_toolbar_report"]/div[1]/span[1]').click()
# time.sleep(5)
# driver.quit()