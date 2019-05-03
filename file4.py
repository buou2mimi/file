# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 12:46
# 文件名称：file4.py
# 开发软件：PyCharm
prompt = "\nPlease enter your name:"
prompt += "\nIf your want to quit enter q,Q or space."

while True:
    name = input(prompt)

    if name == 'q' or name == 'Q' or name == '':
        break
    print("Hello,{}".format(name.title()))
    filename = 'guest.txt'
    with open(filename,'a') as file_object:
        file_object.write(name.title()+'\n')