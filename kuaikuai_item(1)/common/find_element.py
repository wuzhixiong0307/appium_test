from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AppPage():

    def __init__(self,driver):
        self.driver = driver

    def find(self,locator):
        """
        单个元素定位方法封装
        :param locator: {"name":"xxx","by":"id","value":"xxx"}
        :return: 定位方法
        """
        print("正在通过 %s 属性 %s：定位>>%s"%(locator["by"],locator["value"],locator["name"]))
        #text属性定位
        if "text" in locator["by"]:
            t_value = "//*[@text='%s']"%locator["value"]
            t_xpath = ("xpath",t_value)
            element = WebDriverWait(self.driver,30,0.5).\
                until(EC.presence_of_element_located(t_xpath))
        #content-desc属性定位
        elif "desc" in locator["by"]:
            element = WebDriverWait(self.driver,30,0.5).\
                until(lambda x: x.find_element_by_accessibility_id(locator["value"]))
        #uiautomator方法定位,value传值如:'text("登录")'
        elif "uiautomator" in locator["by"]:
            element = WebDriverWait(self.driver,30,0.5).\
                until(lambda x: x.find_element_by_android_uiautomator(locator["value"]))
        #其它属性定位方法：id,xpath,class
        else:
            e_locator = (locator["by"],locator["value"])
            element = WebDriverWait(self.driver,30,0.5).\
                until(EC.presence_of_element_located(e_locator))
        return element