'''最简单的回归模型是线性回归，它是数据挖掘中的基础算法之一。
线性回归的思想是根据数据点形成一个回归函数 y=f(X),函数的参数由数据点通过解方程获得。
线性回归在sklearn库中的基本用法如下。
from sklearn.linear_model import LinearRegression
model = LinearRegression()#建立回归模型
mode1.fit(x,y)#建立回归模型，x是自变量，y是因变量
predicted = model.predict(x_new)#对新样本进行预测
'''
'''很多实际问题都可以归结为逻辑回归问题，即回归函数的y值只有两个可能，也称为二元回归。
逻辑回归可以使用LogisticRegression()函数，接收数据并进行预测。
逻辑回归在sklearn库中的基本用法如下。
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()#建立回归模型
mode1.fit(x,y)#建立回归模型，是自变量，y是因变量
predicted = model.predict(x_new)#对新样本进行预测
'''
'''已知微实例11.1中的10个点，此时获得信息，将在横坐标7的位置出现一个新的点，却不知道纵坐标。
请预测最有可能的纵坐标值。这是典型的预测问题，可以通过回归来实现。
下面给出基于线性回归模型的预测器代码，预测点采用菱形标出。
'''
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
dataSet = np.array ([[1,2],[2,5],[3,4],[4,5],[5,8],[10,13],[11,10],[12,11],[13,15],[15,14]])
x=dataSet[:,0].reshape(-1,1)
y = dataSet[:,1]
linear = linear_model.LinearRegression()
linear.fit(x,y)#根据横纵坐标构造回归函数
x_new = np.array([[7]])
plt.figure (facecolor = 'w' )
plt.axis([0,16,0,16])
plt.scatter(x, y, color='black')#绘制所有点
plt.plot(x,linear.predict(x), color='blue', linewidth=3)
plt.plot(x_new, linear.predict(x_new), 'Dr', markersize=17)
plt.show()




