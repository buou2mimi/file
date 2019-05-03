# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 12:06
# 文件名称：write_message.py
# 开发软件：PyCharm
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games.\n")