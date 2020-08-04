import os,yaml
from common.start_appium import StartAppium

def app_device_cfg(device="huawei"):
    """
    读取手机设备配置信息
    :param device: 设备名称
    :param yamlName: 配置文件名称
    :return: 手机设备配置信息或提示信息
    """
    #获取文件路径
    path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    yaml_url = os.path.join(path,"yaml_cfg_file\devices.yaml")
    print("配置地址：%s" % yaml_url)
    #读取文件
    f = open(yaml_url,"r",encoding="utf-8")
    file = f.read()
    f.close()
    #将yaml文件转换为dict
    data = yaml.load(file,Loader=yaml.FullLoader)
    #启动服务
    for i in data:
        if device in i["desc"]:
            print(i)
            # StartAppium(port=i["port"])
            return i
        # else:
        #     return "配置文件里没有你要的设备：%s"%device

if __name__ == "__main__":
    a = app_device_cfg(device="huawei")
    print(a)
