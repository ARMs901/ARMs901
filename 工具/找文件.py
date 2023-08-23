import os

path = 'C:'
filename = input("请输入文件名：")
result = []

# 将查询结果直接输出
def find_file():
    i = 0
    for root, lists, files in os.walk(path):
        for file in files:
            if filename in file:
                i = i + 1
                write = os.path.join(root, file)
                print('%d %s' % (i, write))
                result.append(write)

# 将查询结果保存在文本文档中
def find_file_and_putin_txt():
    i = 0
    open('E:\Python\\find_file.txt', mode='w').close()
    for root, lists, files in os.walk(path):
        for file in files:
            if filename in file:
                i = i + 1
                write = os.path.join(root, file)

                file_txt = open('C:\用户\\find_file.txt', mode='a+')
                file_txt.write('%d %s \n' % (i, write))
                result.append(write)


if __name__ == '__main__':
    find_file()
    find_file_and_putin_txt()
