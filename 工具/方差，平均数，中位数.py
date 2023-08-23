from math import sqrt
def getNum():
    nums=[]
    iNumStr=input("请输入数字（直接输入，回车退出）：")
    while iNumStr!="":
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字（直接输入，回车退出）：")
    return nums
def mean(numbers):
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return sqrt(sdev/(len(numbers)-1))
def median(numbers):
    new=sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(new[size//2-1]+new[size//2])/2
    else:
        med=new[size//2]
    return med
if __name__=='__main__':
    n=getNum()
    m=mean(n)
    print("平均值：{},方差：{:.2},中位数：{}.".format(m,dev(n,m),median(n)))

