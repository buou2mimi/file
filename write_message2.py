# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 12:15
# 文件名称：write_message2.py
# 开发软件：PyCharm
filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")