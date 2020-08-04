import unittest
from appium import webdriver
from common.find_element import AppPage
from common.read_devices import app_device_cfg
from page.my_page import MyCodeLoginPage,MyPwdLoginPage
from common.start_appium import StartAppium
from tomorrow import threads
import time

#读取手机配置参数
devices = ["leidian", "vivo"]
a = []
for i in devices:
    cfg = app_device_cfg(device=i)
    a.append(cfg)
phone = ["15777936597","19960378307"]

class MyTestCase(unittest.TestCase):
    """
    快快登录测试
    """

    def setUp(self):
        """
        初始化相关环境
        :return:
        """
        #启动app
        element_1 = a.pop()
        self.driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub" % element_1["port"], element_1["des"])
        self.element = AppPage(self.driver)
        self.phone = phone.pop()
        print(element_1)
        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.quit()


    def test_login(self):
        """
        登录失败案例
        :return:
        """
        time.sleep(5)
        self.element.find(MyCodeLoginPage.my).click()
        self.element.find(MyCodeLoginPage.pwd_login).click()
        time.sleep(5)
        self.element.find(MyPwdLoginPage.phone).send_keys(self.phone)
        self.element.find(MyPwdLoginPage.pwd).send_keys("123456")
        self.element.find(MyPwdLoginPage.login_button).click()
        #断言登录失败，还在登录页面
        text = self.element.find(MyPwdLoginPage.forget_pwd).text
        self.assertEqual(text,"忘记密码？")



if __name__ == '__main__':
    unittest.main()
