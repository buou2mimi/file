# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/1 18:33
# 文件名称：file1.py
# 开发软件：PyCharm
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

filename = 'learning_python.txt'
with open(filename)as file_object2:
    for line in file_object2:
        print(line.rstrip())

filename2 = 'learning_python.txt'
with open(filename2) as file_object3:
    lines = file_object3.readlines()
learningnote = ''
for line in lines:
    learningnote += line
print(learningnote.strip())

