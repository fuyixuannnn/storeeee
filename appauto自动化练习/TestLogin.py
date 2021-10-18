from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
from Initpage import Initpage
from LoginPage import LoginPage
import time


@ddt
class TestLogin(TestCase):

    server = r'http://localhost:4723/wd/hub'  # Appium Server, 端口默认为4723
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:21503',
        'platformVersion': '7.1.2',
        'appPackage': 'com.sina.weibo',
        'appActivity': 'com.sina.weibo.SplashActivity',
        'unicodeKeyboard': True,  # 这句和下面那句是避免中文问题的
        'resetKeyboard': True
    }

    # 在每个操作之前先做预备工作
    def setUp(self) -> None:
        self.imgs = []
        self.driver = webdriver.Remote(self.server, self.desired_capabilities)  # 连接手机和APP
        time.sleep(3)  # 等待app启动

    # 在每个用例执行后，将app关闭
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()  # 退出app

    # 登录用例
    @data(*Initpage.login_data)
    def testLogin(self, testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = LoginPage(self.driver)
        login.login(username, password)

        #  获取实际结果
        result = login.login_data()
        time.sleep(1)

        # 与预期结果不符则截图
        if result != expect:
            self.imgs.append(self.driver.get_screenshot_as_base64())
        # 断言
        self.assertEqual(expect, result)
