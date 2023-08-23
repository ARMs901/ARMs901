def h():
    print("123")
def hb(n):
    h()
    h()
    print("456,dear{}".format(n))
    h()
hb("mike")
print()#print 在语句中为空表示输出结果时空一行'''
print()
hb("lily")

#def 函数封装的情况下，计算机不会优先读取函数中的语句内容，上述程序首先读取第八行，hb（n），其中n=Mike调用def hb函数进去函数循环体hb（）
#在hb（）中继续调用h（）函数完成循环打印。
#代码中name是形参，是用来指代要输入的函数实际变量；实际输入的Mike与Lily是实参，代替了形参name，用于函数执行。