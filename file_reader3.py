# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/1 14:39
# 文件名称：file_reader3.py
# 开发软件：PyCharm
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())