#1.1字符串拼接，接受用户输入的两个字符，将他们组合输出。
a=input("请输入名字：")
b=input("请输入专业：")
c=a+b
print(c)
#1.2整数序列求和，用户输入一个正整数N，计算从1到N（包含1和N）相加之后的结果。
n=input("请输入一个正整数N:")
sum=0
for i in range(int(n)):
    sum+=i+1
print("从1到N的就和结果是：",sum)





