'''函数三要素：
函数名
函数参数
返回值'''

'''定义函数的时候参数为形参
调用函数的时候参数为实参'''

def happy():
    print("happy birthday to you！")
def happy_name(name):
    print("祝{}生日快乐".format(name))
    happy()
    happy()
    happy()
    print("happy birthday,dear",name)
    happy()
if __name__=='__main__':
    happy_name("mike")
    happy_name("lily")

