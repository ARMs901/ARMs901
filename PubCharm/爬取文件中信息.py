with open(r'C:\Users\MOMO\OneDrive\桌面\文献简介副本.txt', 'r', encoding='utf-8') as summary_file:
    compounds = []  # 用于累加所有的化合物
    for line in summary_file:
        if 'Compound:' in line:
            current_compounds = line.strip().replace('Compound:', '').split(', ')
            compounds.extend(current_compounds)  # 将当前行的化合物添加到 compounds 中

    with open(r'C:\Users\MOMO\OneDrive\桌面\文献化合物.txt', 'w', encoding='utf-8') as compound_file:
        for compound in compounds:
            compound_file.write(compound.strip() + '\n')
