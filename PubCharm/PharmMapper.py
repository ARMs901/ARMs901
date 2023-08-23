from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

chrome_driver_path = r'C:\anaconda\chromedriver\chromedriver.exe'

url = 'http://lilab-ecust.cn/pharmmapper/index.html'

folder_path = r'C:\Users\MOMO\OneDrive\桌面\连花清瘟mate相关\3D结构'

chrome_driver_path = r'C:\anaconda\chromedriver\chromedriver.exe'

url = 'http://lilab-ecust.cn/pharmmapper/index.html'

folder_path = r'C:\Users\MOMO\OneDrive\桌面\连花清瘟mate相关\3D结构'

options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.implicitly_wait(10)

driver.get(url)

for filename in os.listdir(folder_path):
    if filename.endswith('.sdf'):
        file_path = os.path.join(folder_path, filename)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'jobbtn'))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inputFile'))).send_keys(file_path)

        driver.find_element(By.ID, 'userEmail').send_keys('1981267334@qq.com')
        driver.find_element(By.ID, 'jobname').send_keys(filename)

        driver.find_element(By.ID, 'submit').click()

        time.sleep(10)

driver.quit()
