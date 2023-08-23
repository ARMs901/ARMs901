import os

def batch_change_extension(folder_path, old_extension, new_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(old_extension):
            old_filepath = os.path.join(folder_path, filename)
            new_filename = filename.replace(old_extension, new_extension)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {old_filepath} to {new_filepath}")

# 设置文件夹路径、旧后缀和新后缀
folder_path = "H:\BaiduNetdiskDownload"
old_extension = ".webp"
new_extension = ".jpg"

batch_change_extension(folder_path, old_extension, new_extension)
