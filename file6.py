# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 20:28
# 文件名称：file6.py
# 开发软件：PyCharm
print("Please enter two numbers and I'll add them.")
first_number = input("First number:")
second_number = input("Second number:")
try:
    sum = int(first_number) + int(second_number)
except ValueError:
    print("Sorry,your input is not all numbers.")
else:
    print(sum)