# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 21:20
# 文件名称：file10.py
# 开发软件：PyCharm
filename = 'alice.txt'

with open(filename) as f_ob:
    contents = f_ob.read()
print(contents.lower().count('the'))