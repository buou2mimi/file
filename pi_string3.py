# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/1 17:30
# 文件名称：pi_string3.py
# 开发软件：PyCharm
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    origin_location = pi_string.find(birthday)
    true_location = origin_location - 1
    print(true_location)
else:
    print("Your birthday does not appear in the first million digits of pi.")