import requests
import re

# 输入文件路径和输出文件路径
input_file = r"C:\Users\MOMO\OneDrive\桌面\文献PMID.txt"
output_file = r"C:\Users\MOMO\OneDrive\桌面\文献简介.txt"

# 读取输入文件中的PMID列表
with open(input_file, 'r') as f:
    pmids = f.readlines()

# 对每一个PMID，从NCBI的PubMed下载对应文献并保存到输出文件中
with open(output_file, 'w') as f:
    for pmid in pmids:
        pmid = pmid.strip()
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/?format=abstract"
        response = requests.get(url)
        if response.status_code == 200:
            # 使用正则表达式提取文献摘要部分
            abstract = re.search('<div class="abstract-content selected" tabindex="0">(.*?)</div>', response.text, re.DOTALL)
            if abstract:
                abstract = abstract.group(1).strip()
                f.write(f"PMID: {pmid}\n{abstract}\n\n")
            else:
                print(f"无法提取PMID为{pmid}的文献摘要")
        else:
            print(f"无法下载PMID为{pmid}的文献")
