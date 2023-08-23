import networkx as nx
import numpy as np
import scipy.sparse as sp

#创建一个图
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)])

#计算PageRank值
pr = nx.pagerank(G)

#找出PageRank值最大的节点
max_pr_node = max(pr, key=pr.get)

print("最关键节点是：", max_pr_node)
