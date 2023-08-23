#通过临时重写配置文件的方法，可以解决 Matplotlib 显示中文乱码的问题，代码如下所示：
#绘制折线图
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #正常显示负号;解决中文乱码问题添加这两行代码
year = [2017, 2018, 2019, 2020]
people = [20, 40, 60, 70]
#生成图表
plt.plot(year, people)
plt.xlabel('年份')
plt.ylabel('人口')
plt.title('人口增长')
#设置纵坐标刻度
plt.yticks([0, 20, 40, 60, 80])
#设置填充选项：参数分别对应横坐标，纵坐标，纵坐标填充起始值，填充颜色
plt.fill_between(year, people, 20, color = 'green')
#显示图表
plt.show()