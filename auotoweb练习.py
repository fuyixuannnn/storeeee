'''
    任务：
        1.百度上搜索点
        2.滑动验证其他的都用自动化来做
        3.京东搜索一个商品，点击详情。
'''

# 百度一下
# from selenium import webdriver
# import time
# wd = webdriver.Chrome()
#
# wd.get("http://www.baidu.com")
# wd.maximize_window()
#
# wd.find_element_by_xpath("//*[@id='kw']").send_keys("Justin Bieber")
# wd.find_element_by_xpath("//*[@value='百度一下']").click()
#
# time.sleep(20)
# wd.quit()

# 输入框+提交文件+弹框
# import time
# from selenium import webdriver
# wd = webdriver.Chrome()
# wd.get(r"file:///Users/yixuanfu/Desktop/自动化day01/练习的html/上传文件和下拉列表/autotest.html")
# wd.maximize_window()
#
# wd.find_element_by_xpath("//*[@id='accountID']").send_keys("yixuan fu")
# wd.find_element_by_xpath("//*[@id='passwordID']").send_keys("0000")
# wd.find_element_by_xpath("//*[@id='areaID']").send_keys("天津市")
# wd.find_element_by_xpath("//*[@id='sexID2']").click()
# wd.find_element_by_xpath("//*[@value='Auterm']").click()
#
# wd.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"/Users/yixuanfu/Desktop/！/一寸照片.jpg")
#
# wd.find_element_by_xpath("//*[@id='buttonID']").click()
# time.sleep(3)
# wd.switch_to.alert.accept()
#
# wd.quit()

# 京东
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

wd = webdriver.Chrome()
wd.get("http://www.jd.com")
wd.maximize_window()

wd.find_element_by_xpath("//*[@id='key']").send_keys("大黄蜂手办")
wd.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()

image = wd.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img")
ActionChains(wd).click(image).perform()

time.sleep(10)
wd.quit()
