from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# 设置Chrome浏览器的路径
driver_path = "/path/to/chromedriver"

# 创建一个Chrome浏览器实例
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
service = webdriver.chrome.service.Service(executable_path=driver_path)
driver = webdriver.Chrome(executable_path=driver_path)


# 打开网页
driver.get("https://old.tcmsp-e.com/tcmspsearch.php?qr=Lonicerae%20Japonicae%20Flos&qsr=herb_en_name&token=2c94db7bcf88f4727dc936a6a2108beb")
time.sleep(2)

# 创建一个空列表，用于保存所有化合物名称
molecule_names = []

# 遍历所有16页
for i in range(1, 17):
    # 获取当前页的HTML内容
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 获取所有Mol ID
    mol_ids = [a.text for a in soup.select("#Ingredients a")]

    # 遍历所有Mol ID
    for mol_id in mol_ids:
        # 打开Molecule详情页
        driver.get(f"https://old.tcmsp-e.com/mol.php?mol_id={mol_id}")

        # 获取Molecule名称
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        molecule_name = soup.select_one(".detailname").text

        # 将Molecule名称加入列表
        molecule_names.append(molecule_name)


    # 点击下一页按钮
    next_button = driver.find_element_by_css_selector(".k-icon.k-i-arrow-e")
    next_button.click()
    time.sleep(2)

# 关闭浏览器
driver.quit()

# 将所有Molecule名称保存到文件
with open("C:\\Users\\MOMO\\OneDrive\\桌面\\金银花MOID.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(molecule_names))
