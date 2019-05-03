# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 10:26
# 文件名称：remember_me3.py
# 开发软件：PyCharm
import json

def greet_user():
    """问候用户，并指出名字"""
    filename = 'username.json'
    try:
        with open(filename,'r') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name?")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back,{}!".format(username))
    else:
        print("Welcome back,{}!".format(username))