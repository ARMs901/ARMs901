import networkx as nx
import numpy as np
#import matplotlib.pyplot as plt

# 创建一个空的无向图
G = nx.Graph()

# 添加节点
"""G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# 添加边
edges = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 10), (2, 4), (2, 5), (2, 6), (2, 9), (3, 7), (3, 8), (4, 7), (4, 5), (4, 10), (5, 10), (6, 10), (6, 9), (7, 10), (8, 9), (9, 10), (10, 11)]
G.add_edges_from(edges)"""

G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

# 添加边
edges = [(1, 3), (2, 7), (3, 4), (3, 7), (3, 12), (4, 7), (4, 8), (4, 9), (4, 12), (4, 13), (5, 7), (5, 8), (5, 12), (6, 7), (6, 11), (7, 8), (7, 9), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), (7, 18), (8, 9), (8, 12), (8, 13), (8, 14), (9, 12), (9, 13), (9, 14), (9, 10), (12, 13), (12, 15), (12, 16), (13, 16), (13, 17), (13, 18), (13, 19), (14, 17), (15, 16), (15, 17), (15, 18), (15, 19), (16, 17), (16, 18), (16, 19), (17, 18), (17, 19), (18, 19)]
G.add_edges_from(edges)

# 绘制图形
#nx.draw(G, with_labels=True)
#plt.show()
# 计算每个节点的接近中心性
# 计算节点度、节点介数中心性和节点接近中心性
'''degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# 将这三个特征组合成一个向量
features = np.array([list(degree_centrality.values()), list(betweenness_centrality.values()), list(closeness_centrality.values())]).T

print(features)'''

# 计算PageRank值
pr = nx.pagerank(G)

# 找出PageRank值最大的节点
max_pr_node = max(pr, key=pr.get)

print("最关键节点是：", max_pr_node)