#1.4计算一到十阶乘相加的结果
sum=0
tmp=1
for k in range(1,11):
    tmp*=k
    sum+=tmp
print("输出结果为：{}".format(sum))

#注意format的格式用法，阶乘和相加看清楚运算对象。
#计算阶乘，要求用户随意输入数字
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=eval(input("请输入一个整数："))
print(fact(abs(int(num))))#abs函数的意思是绝对值
#计算了累加，要求客户输入任意正整数

def sm(i):
    if i<=1:
        return i
    else:
        s=0
        for j in range(i+1):
            s+=j
        return s
s=eval(input("请输入一个正整数："))
print(sm(int(s)))
'''循环要有结束输出或者打破，在函数体中，用return输出结果，
若是用print结果会重复输出并且因为没有函数体的结果输出，会报错输出none
在python中，一个print对应了一个输出，在不必要的情况下，注意print输出的使用，重复的输出会影响结果的判断'''