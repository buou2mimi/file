# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 12:54
# 文件名称：file5.py
# 开发软件：PyCharm
prompt = "Why do you like programming?"
prompt += "\nIf you want to quit,please enter q,Q or nothing."

while True:
    reason = input(prompt)
    if reason == 'q' or reason == 'Q' or reason =='':
        break
    filename = "reasons.txt"
    with open(filename,'a') as file_object:
        file_object.write(reason +'\n')