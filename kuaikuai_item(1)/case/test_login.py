from appium import webdriver
from time import sleep
from common.find_element import AppPage
from page.my_page import MyCodeLoginPage,MyPwdLoginPage
from common.read_devices import app_device_cfg
from tomorrow import threads

@threads(2)
def run_app(deviceName,pohe):
    """
    运行脚本
    :param deviceName:
    :return:
    """
    #获取配置参数
    des = app_device_cfg(device=deviceName)
    driver = webdriver.Remote("http://127.0.0.1:%s/wd/hub" %des["port"],des["des"])
    e = AppPage(driver)
    e.find(MyCodeLoginPage.my).click()
    e.find(MyCodeLoginPage.pwd_login).click()
    sleep(3)
    e.find(MyPwdLoginPage.phone).send_keys(pohe)
    e.find(MyPwdLoginPage.pwd).send_keys("123456")
    e.find(MyPwdLoginPage.login_button).click()
    driver.quit()

if __name__ == "__main__":
    from common.start_appium import StartAppium
    host = "127.0.0.1"
    for i in range(2):
        port = 4723 + 2 * i
        StartAppium(host, port)
    # 运行脚本
    devices = ["xiaomi", "huawei"]
    for i in devices:
        run_app(deviceName=i)

