# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 20:38
# 文件名称：file7.py
# 开发软件：PyCharm
print("Please enter two numbers and I'll add them.")
while True:
    try:
        first_number = input("First number:")
        if first_number == 'q':
            break
        first_number = int(first_number)
        second_number = input("Second number:")
        if second_number == 'q':
            break
        second_number = int(second_number)

    except ValueError:
        print("Sorry,your input is not all numbers.")
    else:
        sum = first_number + second_number
        print(sum)