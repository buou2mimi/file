# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 10:58
# 文件名称：remember_me5.py
# 开发软件：PyCharm
import json

def get_stored_usrname():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename,'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_usrname()
    if username:
        print("Welcome back,{}!".format(username))
    else:
        username =get_new_username()
        print("We'll remember you when you come back,{}!".format(username))

greet_user()