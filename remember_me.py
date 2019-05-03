# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 10:03
# 文件名称：remember_me.py
# 开发软件：PyCharm
import json

username = input("What is your name?")

filename ='username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back,{}!".format(username))