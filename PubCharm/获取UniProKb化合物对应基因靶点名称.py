import requests
from bs4 import BeautifulSoup
import time

# 读取蛋白质名称
with open('C:\\Users\\MOMO\\OneDrive\\桌面\\蛋白质靶点.txt') as f:
    protein_names = f.read().splitlines()

# 去重
protein_names = list(set(protein_names))

# 初始化基因名称列表
gene_names = []

# 循环遍历蛋白质名称列表
for protein_name in protein_names:
    # 构造搜索URL
    search_url = f'https://www.uniprot.org/uniprot/?query={protein_name}&sort=score'
    # 发送GET请求
    response = requests.get(search_url)
    # 解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')
    # 查找基因名称
    gene_name_tags = soup.find_all('a', {'class': 'entryName'})
    for gene_name_tag in gene_name_tags:
        gene_name = gene_name_tag.text
        # 去重并保存基因名称
        if gene_name not in gene_names:
            gene_names.append(gene_name)

    # 避免被网站限制频率
    time.sleep(5)

# 将基因名称写入文件
with open('C:\\Users\\MOMO\\OneDrive\\桌面\\基因靶点.txt', 'w') as f:
    f.write('\n'.join(gene_names))
