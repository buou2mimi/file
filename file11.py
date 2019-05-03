# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 11:18
# 文件名称：file11.py
# 开发软件：PyCharm
import json

filename = 'favorite_number.json'
favorite_number = input("Enter your favorite numeber:")

with open(filename,'w') as f_obj:
    json.dump(favorite_number,f_obj)
    print("I'll remember that the number is {}.".format(favorite_number))

with open(filename,'r') as f_obj:
    favorite_number = json.load(f_obj)
    print("I konw your favorite number!It's {}.".format(favorite_number))