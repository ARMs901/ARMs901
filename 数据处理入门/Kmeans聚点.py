'''微实例11.1:10个点的聚类。
假设有10个点:(1,2)(2,5),(3,4),(4,5),(5,8),(10,13),(11,10),(12,11),(13,15),(15,14)，
请将它们分成2类，并绘制聚类效果。采用KMeans方法，代码如下。
'''

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
dataSet = np.array ([[1,2],[2,5],[3,4],[4,5],[5,8],[10,13],[11,10],[12,11],[13,15],[15,14]])
km = KMeans(n_clusters=2)
km.fit(dataSet)
plt.figure (facecolor = 'w')
plt.axis ([0,16,0,16])
mark = ['or','ob']
for i in range (dataSet.shape[0]):
    plt.plot(dataSet[i,0], dataSet[i,1], mark[km.labels_[i]])
plt.show()

'''KMeans基本用法如下。
from sklearn.cluster import KMeans
model= KMeans()#输入参数建立模型
mode1.fit(Data)#将数据集Data提供给模型进行聚类'''

'''AgglomerativeClustering使用方法如下:此外，还有基于层次的聚类方法，该方法将数据对象组成一棵聚类树，
采用自底向上或自顶向下方式遍历，最终形成聚类
from sklearn.cluster import Agglomerativeclustering
model = Agglomerativeclustering()#输入参数建立模型
mode1.fit(Data)#将数据集Data提供给模型进行聚类'''

'''DBSCAN使用方法如下:DBSCAN是一个基于密度的聚类算法。
from sklearn.cluster import DBSCAN
model = DBSCAN ( )#输入参数建立模型
mode1.fit(Data)#将数据集Data提供给模型进行聚类'''



