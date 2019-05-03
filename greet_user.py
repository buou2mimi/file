# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 10:12
# 文件名称：greet_user.py
# 开发软件：PyCharm
import json

filename = 'username.json'

with open(filename,'r') as f_obj:
    username = json.load(f_obj)
    print("Welcome back,{}!".format(username))