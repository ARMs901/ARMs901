'''52张牌任取四张牌计算后结果为21，
让用户随意输入四张牌，判定这四张牌成为21点的方式或失败，输出结果'''

solutions = set()

def point21(numbers):
    global solutions
    if len(numbers) == 1:
        if abs(eval(numbers[0]) - 21) < 0.00001:
            solutions.add(numbers[0])
    else:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                rest_numbers = [x for p, x in enumerate(numbers) if p != i and p != j]
                for op in "+-*/":
                    if op in "+-*" or eval(str(numbers[j])) != 0:
                        point21(["("+ str(numbers[i]) + op + str(numbers[j]) + ")"] + rest_numbers)
                        if op == "-" or (op == "/" and eval(str(numbers[i])) != 0):
                            point21(["("+ str(numbers[j]) + op + str(numbers[i]) + ")"] + rest_numbers)

x = input('请输入四张点数（中间以英文逗号隔开）：')
x_lst = x.split(',')
point21(x_lst) # 测试用例
print("Found %d solutions." %len(solutions))
for i, s in enumerate(solutions):
    print("%d: %s = 21" %(i+1, s))