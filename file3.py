# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 12:20
# 文件名称：file3.py
# 开发软件：PyCharm
prompt = "\nPlease enter your name:"
prompt += "\nIf your want to quit enter q,Q or space."

name = input(prompt)

filename = 'guest.txt'
with open(filename,'a') as file_object:
        file_object.write(name+'\n')