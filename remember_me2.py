# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 10:21
# 文件名称：remember_me2.py
# 开发软件：PyCharm
import json
#如果以前存储了用户名，就加载它
#否则，就提示用户输入名并存储它

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
    print("Welcome come back,{}!".format(username))