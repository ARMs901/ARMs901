'''第一步，从sklearn 库中导入 datasets类，然后调用它的load_iris()方法读取IRIS数据集并赋给变量 iris。
同时，将iris变量的data成员赋给dataSet变量。可以通过print(dataSet)语句打印IRIS数据集内容。

from sklearn import datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris ()
dataSet = iris.data

第二步，获取用户输入的聚类个数k以及最大迭代次数iterNum。
第三步，调用Sklearn的K均值方法聚类数据集dataSet，这两步代码如下。

from sklearn.cluster import KMeans
k = eval (input( "请输入K值:"))
iterNum = eval(input("请输入最大迭代次数:"))
model= KMeans(n_clusters=k, init='random ' , max_iter=iterNum)
model.fit(dataSet)#对数据集开始聚类

第四步，为了将聚类结果显示出来，定义显示函数showCluster()，将聚类结果用不同颜色显示在坐标系中。
该函数首先计算数组dataSet的行数和列数，并定义5种颜色，然后利用for循环根据类别绘制每个样本点，
最后利用for循环把每个中心点以更大的尺寸绘制出来，该函数代码如下。

def showCluster (dataSet, k, centers, clusters) :
    plt.figure(facecolor = 'white ')
    num,nattr = dataSet.shape#数据个数和属性个数
    mark = [ ' or ' , ' ob' , 'og ' , ' om ' , 'oy ']#聚类颜色
    for i in range (num) :
        plt.plot(dataSet[i,0] , dataSet[i,1 ] ,mark [int(clusters[i]) ])
    mark = [ 'Dr', 'Db', 'Dg', ' Dm ', 'Dy ']
    for i in range(k) : #绘制K均值各簇中心点
        plt.plot(centers[i,0] , centers[i,1] ,mark[i] ,markersize = 17)
    plt.title( "在iris数据集上的K均值聚类")
    plt.xlabe1( "尊片长度")
    plt.ylabel("尊片宽度")
    plt.show ( )

将尊片长度作为横轴，尊片宽度作为纵轴，以二维方式将聚类结果展现出来，
其中，每种颜色代表一种分类。由于K均值的初始簇中心点是随机选取的，有可能出现多次运行结果不一致的情况，
'''
#整合代码如下：
#e22.1ClusterIRIS.py
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib
import numpy as nps
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['simHei']

def showCluster(dataSet,k,centers,clusters):
    plt.figure(facecolor='white')
    num,nattr = dataSet.shape#数据个数和属性个数
    mark = ['or','ob','og','om','oy']#聚类颜色
    for i in range(num):
        plt.plot(dataSet[i,0],dataSet[i,1],mark[int(clusters[i])])
    mark = ['Dr','Db','Dg','Dm','Dy']
    for i in range(k):#绘制K均值各簇中心点
        plt.plot(centers[i,0],centers[i,1],mark[i],markersize=17)
    plt.title("IRIS数据集的K均值聚类")
    plt.xlabel("花瓣长度")
    plt.ylabel("花瓣宽度")
    plt.show()

def main():
    iris = datasets.load_iris()
    dataSet = iris.data
    k = eval(input("请输入K值:"))
    iterNum = eval(input("请输入最大迭代次数:"))
    model = KMeans(n_clusters=k,init='random',max_iter=iterNum)
    model.fit(dataSet)#对数据集开始聚类
    showCluster(dataSet,k,model.cluster_centers_,model.labels_)
main()

