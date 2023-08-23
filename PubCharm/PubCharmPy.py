import os
import requests
import time

# 定义函数，用于根据化合物名称获取其 PubChem CID
def get_cid(name):
    # 构建获取化合物 CID 的 URL
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/cids/JSON'
    # 发送请求，获取响应
    response = requests.get(url)
    # 如果响应状态码为200，则表示请求成功
    if response.status_code == 200:
        # 解析 JSON 数据，获取化合物 CID
        data = response.json()
        cid = data['IdentifierList']['CID'][0]
        # 返回化合物 CID
        return cid
    else:
        # 如果请求失败，抛出异常
        raise Exception(f'Failed to get CID for compound {name}')

# 定义函数，用于获取化合物的3D结构信息
def get_compound_3d(cid):
    # 构建获取化合物3D结构信息的URL
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/record/SDF/?record_type=3d'
    # 发送请求，获取响应
    response = requests.get(url)
    # 如果响应状态码为200，则表示请求成功
    if response.status_code == 200:
        # 返回响应内容
        return response.content
    else:
        # 如果请求失败，抛出异常
        raise Exception(f'Failed to get compound {cid} 3D structure')

# 创建保存 SDF 文件的目录
if not os.path.exists('sdf_files'):
    os.mkdir('sdf_files')

# 读取化合物名称列表文件
with open('C:\\Users\\MOMO\\OneDrive\\桌面\\compound_names.txt', 'r', encoding='utf-8') as f:
    compound_names = f.read().splitlines()

# 循环遍历每个化合物名称，获取其3D结构信息并保存到文件
for name in compound_names:
    try:
        # 获取化合物 CID
        cid = get_cid(name)
        # 获取化合物的3D结构信息
        sdf_data = get_compound_3d(cid)
        # 保存到文件
        with open(f'sdf_files/{name}.sdf', 'wb') as f:
            f.write(sdf_data)
    except Exception as e:
        print(f'Error occurred while getting 3D structure for {name}: {str(e)}')

