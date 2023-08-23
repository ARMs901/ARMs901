import random
import time
count = 0

start = time.perf_counter()
f=int(input("请输入点数："))
for i in range(0,f):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x*x + y*y)**(1/2) < 1:
        count=count+1
pi = (4*count/f)
print("frequency:",f)
print("pi = {:.5f}".format(pi))
print("time: {:.5f}s".format(time.perf_counter()-start))
