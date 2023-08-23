import os  # 只需要引入这个系统控制的库

# 定义一个path变量，里面是存着所以需要改的txt文件的文件夹名称
path = 'C:\Users\MOMO\Desktop\新冠病毒学习\分析基因序列的一些学习知识'
# 系统列表出所有path文件夹里面文件的名称 （此操作并不会有序遍历所有文件，因此需要下一条代码排列）
total_txt = os.listdir(path)
# 通过文件名格式前的数字大小按升序排列
total_txt.sort(key=lambda x: int(x.split('.')[0]))
deleteList = []  # 设定变量deleteList，随后print出来
