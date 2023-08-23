import numpy as np
##定义字段名score，以及数组数据类型i1
dt = np.dtype([('score','i1')])
a = np.array([(55,),(75,),(85,)], dtype = dt)
print("获取a数组:"'\n',a)
print("数据类型对象dtype"'\n',a.dtype)
print("获取'score'字段分数"'\n',a['score'])