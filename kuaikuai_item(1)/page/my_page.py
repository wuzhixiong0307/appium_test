
class MyCodeLoginPage:
    """
    我的-验证码登录页面元素
    """
    my = {"name":"我的","by":"text","value":"我的"}
    phone = {"name":"我的-手机号码","by":"text","value":"请输入11位手机号"}
    code = {"name":"我的-验证码","by":"id","value":"com.tckk.kk:id/edit_identifying_code"}
    code_button ={"name":"我的-验证码按钮","by":"id","value":"com.tckk.kk:id/identifying"}
    login = {"name":"我的-登录按钮","by":"id","value":"com.tckk.kk:id/login"}
    pwd_login = {"name":"我的-密码登录","by":"id","value":"com.tckk.kk:id/pwd_login"}

class MyPwdLoginPage:
    """
    我的-密码登录页面元素
    """
    phone = {"name":"我的-手机号码","by":"text","value":"请输入11位手机号"}
    pwd = {"name":"我的-密码","by":"id","value":"com.tckk.kk:id/input_pwd"}
    login_button = {"name":"我的-登录","by":"id","value":"com.tckk.kk:id/login"}
    forget_pwd = {"name":"我的-忘记密码","by":"id","value":"com.tckk.kk:id/forget_pwd"}
    back = {"name":"我的-返回","by":"id","value":"com.tckk.kk:id/back"}