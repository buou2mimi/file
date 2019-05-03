# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/1 19:09
# 文件名称：file2.py
# 开发软件：PyCharm
filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
message = ''
for line in lines:
    message += line
print(message.replace('Python','C'))