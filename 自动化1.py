'''
任务1：
        实现京东搜索一个商品，点击详情，点击添加购物车
        苏宁的搜索一个商品，点击详情，添加购物车，登陆一下。
        b站先登录，搜索一个鬼畜视频，点个赞。
'''
from selenium import webdriver

a = webdriver.Chrome()
# a.get('https://www.jd.com/')
# a.maximize_window()
# a.find_element_by_id("key").send_keys("斩首大刀")
# a.find_element_by_xpath("//*[@class='button']").click()
# a.find_element_by_xpath("//*[@href='//item.jd.com/62869686135.html]").click()
# a.find_element_by_id('InitCartUrl').click()

# a.get('https://www.suning.com/')
# a.maximize_window()
# a.find_element_by_id('searchKeywords').send_keys('天锁斩月')
# a.find_element_by_id('searchSubmit').click()
# a.find_element_by_name('ssdsn_search_pro_name02-1_0_0_12310123534_0071489682').click()
# a.find_element_by_name('item_12310123535_gmq_buy01').click()

a.get('https://www.bilibili.com/')
a.maximize_window()
a.find_element_by_xpath("//*[autocomplete='off']").send_keys('后撤步')
a.find_element_by_xpath(("//*[class='nav-search-btn']"))
a.find_element_by_xpath("//*[style='background-position: -1344px 10px; opacity: 0; background-image: url('//i0.hdslb.com/bfs/videoshot/301324537.jpg@85q.webp'); background-size: 1680px;']")
a.find_element_by_xpath("//*[class='like']").click()


