import requests
# import urllib.parse  # urllib用以解码中药材名称，是否需要见具体需求
from bs4 import BeautifulSoup
import re
import xlsxwriter

class get_drug_target(object):

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        }
        self.base_url = 'http://tcmspw.com/tcmspsearch.php?'

    def get_url(self, drug):
        # 下面注释的是中文解码的过程
        # drug_decode = urllib.parse.quote(drug)
        # url = self.base_url+'qs=herb_all_name&q='+drug_decode+'&token=f8abf58ec1d6b214e0d6ca4ec94ee7d3'
        # 下面是不解码
        url = self.base_url+'qs=herb_all_name&q='+drug+'&token=9b8fe8d60b5028b2eb0ee7e5e7834a40'
        # 请求url
        response = requests.get(url, headers=self.headers)
        data = response.content.decode()
        return data

    def search_drug_url(self, data):
        soup = BeautifulSoup(data, 'lxml')
        # 曲线救国，寻找javascript中的数据
        drug_url1 = soup.find_all('script')
        drug_url1 = str(drug_url1)
        # 获取英文名
        drug_name1 = re.search(r'"herb_en_name":"(.*?)"', drug_url1).group(1)
        # 将英文名之间的空格替换为 %20
        drug_name2 = drug_name1.replace(' ', '%20')
        # 获取url地址
        drug_url2 = re.search(r"href='(.+)'", drug_url1).group(1)
        # 拼接url
        combined_url = 'http://tcmspw.com/' + drug_url2.split('$')[0] + drug_name2 + drug_url2.split('}')[1]
        return combined_url

    def get_target(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'lxml')
        # 一共10个script
        target = soup.find_all('script')[9]
        target = str(target)
        # 两次使用正则获取靶向基因
        target_info = re.search(r'JSON.parse\(\"(.+)\"\)', target).group(1)
        target_info = re.findall(r'label\":\"(.*?)\"', target_info)
        target_list = []
        for t in target_info:
            # 注意这里的pattern我没加r
            target_list.append(t.replace('\\\\', ''))
        print(target_list)
        return target_list

    def run(self):
        drug_list = ['金银花']
        with xlsxwriter.Workbook('TCM.xlsx') as writer:
            sheet = writer.add_worksheet('TCM_target')
            for index, drug in enumerate(drug_list):
                data = self.get_url(drug)
                combined_url = self.search_drug_url(data)
                target_data = self.get_target(combined_url)
            sheet.write_column(1, index, target_data)
            sheet.write(0, index, drug_list[index])
        writer.close()



