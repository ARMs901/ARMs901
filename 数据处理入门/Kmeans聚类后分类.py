'''from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsclassifier()#建立分类器模型
model.fit(Data,y)#为模型提供学习数据Data和数据对应的标签结果y
'''
'''此外，决策树算法也是用于分类的数据挖掘经典算法之一，
常用于特征含有类别信息的分类或回归问题，这种方法非常适合多分类情况。
from sklearn.neighbors import DecisionTreeClassifier
model = DecisionTreeclassifier()#建立分类器模型
model.fit(Data,y)#为模型提供学习数据Data和数据对应的标签结果y
'''
'''微实例11.1两10个点分成了2类A和B。
现在有一个新的点（6，9)，在分类结果A和B的基础上，新的点属于哪一类呢?
采用K临近方法的分类代码如下'''
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
dataSet = np.array( [[1,2],[2,5],[3,4],[4,5],[5,8],[10,13],[11,10],[12,11],[13,15],[15,14]])
km = KMeans(n_clusters=2)
km.fit(dataSet)
labels = km.labels_#使用KMeans聚类结果进行分类
knn = KNeighborsClassifier()
knn.fit(dataSet,labels)#学习分类结果
data_new = np.array([[6,9]])
label_new = knn.predict(data_new)#对点(6,9)进行分类
plt.figure(facecolor = 'w')
plt.axis ([0,16,0,16])
mark = ['or','ob']
for i in range (dataSet.shape[0]):
    plt.plot(dataSet[i,0],dataSet[i,1], mark [labels[i]])
plt.plot(data_new[0,0],data_new[0,1],mark [label_new[0]],markersize=17)
plt.show()




