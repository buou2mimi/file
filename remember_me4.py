# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 10:48
# 文件名称：remember_me4.py
# 开发软件：PyCharm
import json

def get_stored_username():
    """如果存储了用户，就获取它"""
    filename = 'username.json'
    try:
        with open(filename,'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return  None
    else:
        return username

def greet_user():
    """问候用户，并指出其姓名"""
    username = get_stored_username()
    if username:
        print("Welcome come back,{}".format(username))
    else:
        username = input("What is your name?")
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when come back,{}!".format(username))

greet_user()
