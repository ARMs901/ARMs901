import requests
from bs4 import BeautifulSoup
import re

# 允许用户输入关键词
keywords = input("请输入关键词，多个关键词请用空格分隔：").split()

# 拼接搜索链接
search_query = "+".join(keywords)
url = f"https://pubmed.ncbi.nlm.nih.gov/?term={search_query}"

# 发送请求获取搜索结果页面
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# 获取搜索结果中的文章链接
articles = []
for a in soup.find_all("a"):
    if a.get("href") and "/pmid/" in a["href"]:
        articles.append(a["href"])

# 下载符合条件的文章简介
with open("C:\\Users\\MOMO\\OneDrive\\桌面\\文献简介.txt", "w", encoding="utf-8") as f:
    for article in articles:
        response = requests.get(f"https://pubmed.ncbi.nlm.nih.gov{article}")
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("h1", {"class": "heading-title"}).get_text(strip=True)
        abstract = soup.find("div", {"class": "abstract-content selected"}).get_text(strip=True)
        f.write(f"{title}\n{abstract}\n\n")

# 提取PMID并保存到文件
pmids = []
with open("C:\\Users\\MOMO\\OneDrive\\桌面\\文献简介.txt", "r", encoding="utf-8") as f:
    for line in f:
        pmid_match = re.search(r"PMID\s*(\d+)", line)
        if pmid_match:
            pmids.append(f"PMID-{pmid_match.group(1)}")

with open("C:\\Users\\MOMO\\OneDrive\\桌面\\文献PMID.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(pmids))
#请将程序保存为pubmed_search.py文件并运行。
# 在程序运行时，会提示您输入关键词。您可以输入多个关键词，它们应该用空格分隔。
# 程序将搜索PubMed以查找符合条件的文章，并将其简介保存在C:\Users\MOMO\OneDrive\桌面\文献简介.txt文件中，
# 同时将提取的PMID保存在C:\Users\MOMO\OneDrive\桌面\文献PMID.txt文件中。