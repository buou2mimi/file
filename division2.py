# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 13:36
# 文件名称：division2.py
# 开发软件：PyCharm
print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
        print(answer)