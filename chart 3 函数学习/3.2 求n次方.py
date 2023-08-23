'''def power(x, n): #如def power (x,n=2) 设置了n的默认值为2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2, 4))'''

def y (x,n):
    s=1
    for i in range(1,n+1):
        s=s*x

    return s
x=eval(input("输入X："))
n=abs(eval(input("输入N：")))
print(y(x,n))


