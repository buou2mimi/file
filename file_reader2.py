# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/1 14:06
# 文件名称：file_reader2.py
# 开发软件：PyCharm
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())