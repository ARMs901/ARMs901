from Bio import Entrez, Medline
import re

# 输入NCBI邮箱和API密钥
Entrez.email = 'arms7475980818@gmail.com'
Entrez.api_key = '9548b38fa48260e553d15c3e24a2de6a9808'

# 读取化合物名称文件
with open(r'C:\Users\MOMO\OneDrive\桌面\金银花化合物名称.txt', 'r',) as f:
    compound_names = list(set(f.read().splitlines()))

# 构建NCBI搜索query字符串
compound_query = '(' + ' OR '.join(compound_names) + ')'
covid_query = ' COVID-19[Title/Abstract] OR SARS-CoV-2[Title/Abstract]'
search_query = compound_query + ' AND (' + covid_query + ')'

# 搜索PubMed并下载文献
search_handle = Entrez.esearch(db='pubmed', term=search_query, retmax=100000)
search_results = Entrez.read(search_handle)
search_handle.close()

pmids = search_results['IdList']
summary_file = open(r'C:\Users\MOMO\OneDrive\桌面\文献简介.txt', 'w',)

for pmid in pmids:
    summary_handle = Entrez.efetch(db='pubmed', id=pmid, rettype='medline', retmode='text')
    summary = Medline.read(summary_handle)

    summary_file.write('compound: ' + compound_query + '\n')
    summary_file.write('PMID: ' + pmid + '\n')
    summary_file.write('Title: ' + summary.get('TI', '') + '\n')
    summary_file.write('Authors: ' + ', '.join(summary.get('AU', [])) + '\n')
    summary_file.write('Journal: ' + summary.get('JT', '') + '\n')
    summary_file.write('Publication date: ' + summary.get('DP', '') + '\n')
    summary_file.write('Abstract: ' + summary.get('AB', '') + '\n\n')
    summary_handle.close()

summary_file.close()
# 将有搜索结果的化合物名称写入文件
