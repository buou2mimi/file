# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 14:17
# 文件名称：alice.py
# 开发软件：PyCharm
filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry,the file {} does not exit.".format(filename)
else:
    words = contents.split()
    num_words = len(words)
    print("The file {} has about {} words.".format(filename,num_words))