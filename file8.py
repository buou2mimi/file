# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 20:50
# 文件名称：file8.py
# 开发软件：PyCharm
filenames = ["cats.txt","dogs.txt"]

for filename in filenames:
    print("\nReading file:{}".format(filename))
    try:
        with open(filename) as f_ob:
            contents = f_ob.read()
    except FileNotFoundError:
        print("Sorry,I can't find this file.")
    else:
        print(contents)