# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/5/2 14:22
# 文件名称：word_count.py
# 开发软件：PyCharm
def count_word(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry,the file {} does not exist.".format(filename)
        print(msg)
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file {} has about {} words.".format(filename,num_words))

count_word('alice.txt')
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_word(filename)
