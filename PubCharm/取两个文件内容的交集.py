# 读取金银花化合物名称文件
with open(r'C:\Users\MOMO\OneDrive\桌面\金银花化合物名称.txt', 'r', encoding='utf-8') as f:
    compound_names_1 = set(f.read().splitlines())

# 读取文献化合物文件
with open(r'C:\Users\MOMO\OneDrive\桌面\文献化合物.txt', 'r', encoding='utf-8') as f:
    compound_names_2 = set(f.read().splitlines())

# 找到两个文件中的交集
common_compounds = compound_names_1.intersection(compound_names_2)

# 将交集写入新的文件
with open(r'C:\Users\MOMO\OneDrive\桌面\化合物交集.txt', 'w', encoding='utf-8') as f:
    for compound in common_compounds:
        f.write(compound + '\n')
