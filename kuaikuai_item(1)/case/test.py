from appium import webdriver
from time import sleep

desired_caps = {
    "platformName":"Android",   #使用操作系统
    "deviceName":"APH0219724018121",   #设备名称
    "platformVersion":"10",    #系统版本
    "appPackage":"com.tckk.kk",   #apk包名
    "appActivity":"com.tckk.kk.ui.start.SplashActivity",   #apk的launchable-activity
    "noReset":True,   #不清除缓存
    "unicodeKeyboard":True,   #使用unicode编码发送字符串
    "resetKeyboard":True,  #隐藏键盘
    # "automationName":"Uiautomator2"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
sleep(10)
driver.find_element_by_xpath('//*[@text="我的"]').click()
sleep(5)
driver.find_element_by_id("com.tckk.kk:id/pwd_login").click()
sleep(5)
driver.find_element_by_xpath("//*[@text='请输入11位手机号']").send_keys("15777936597")
sleep(5)
driver.find_element_by_id("com.tckk.kk:id/input_pwd").send_keys("12345")
driver.quit()
