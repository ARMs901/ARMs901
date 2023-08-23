#1.3九九乘法表输出，工整打印乘法表，格式不限。
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(j,i,i*j),end='\t')
    print(end='\n')

#注意缩进，有冒号就有缩进