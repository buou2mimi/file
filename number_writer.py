# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/3 9:54
# 文件名称：number_writer.py
# 开发软件：PyCharm
import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)