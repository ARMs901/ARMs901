for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            if i/3 + j *3 + k * 5 == 100 and i+j+k==100:
                print('小鸡',i,'母鸡',j,'公鸡',k)

