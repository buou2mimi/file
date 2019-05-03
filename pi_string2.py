# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/1 17:23
# 文件名称：pi_string2.py
# 开发软件：PyCharm
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))