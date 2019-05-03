# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/1 13:18
# 文件名称：file_reader.py
# 开发软件：PyCharm
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())