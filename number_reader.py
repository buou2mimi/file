# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 9:59
# 文件名称：number_reader.py
# 开发软件：PyCharm
import json

filename = 'numbers.json'
with open(filename,'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)