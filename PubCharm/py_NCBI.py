import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.request import urlretrieve
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置ChromeDriver路径
s = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')  # 无界面模式
options.add_argument('--disable-gpu')  # 禁用GPU加速
driver = webdriver.Chrome(service=s, options=options)

# 定义提取PMID的函数
def extract_pmids(file_path):
    pmids = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            match = re.search(r'PMID- \d+', line)
            if match:
                pmid = match.group().split('- ')[1]
                pmids.append(pmid)
    return pmids

# 搜索并下载PDF文献
def download_pdf(pmid):
    # 进入NCBI主页
    driver.get('https://www.ncbi.nlm.nih.gov/')
    # 在搜索框中输入PMID并搜索
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'term')))
    search_box.send_keys(pmid)
    search_box.submit()
    # 进入搜索结果页面
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'title-link')))
    result.click()
    # 进入文献详情页面
    pdf_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'pdf') and contains(text(), 'Free PMC')]")))
    pdf_link.click()
    # 下载PDF文件
    pdf_url = driver.current_url
    file_name = f'{pmid}.pdf'
    file_path = r'C:\Users\MOMO\OneDrive\桌面\金银花mate相关'
    urlretrieve(pdf_url, os.path.join(file_path, file_name))
    # 返回文献标题
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'citation-title'))).text
    return title

# 遍历文件目录下所有TXT文件
file_path = r'C:\Users\MOMO\OneDrive\桌面\金银花mate相关'
for file_name in os.listdir(file_path):
    if file_name.endswith('.txt'):
        # 提取PMID
        pmids = extract_pmids(os.path.join(file_path, file_name))
        # 下载文献
        for pmid in pmids:
            try:
                title = download_pdf(pmid)
                print(f'{title} (PMID- {pmid}) 下载成功')
            except Exception as e:
                print(f'下载失败：{e}')
            sleep(5)  # 防止下载过快被封IP
