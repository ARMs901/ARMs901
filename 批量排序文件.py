import os
import glob


def rename_files_by_time(folder_path):
    # 获取文件夹中所有文件的路径
    files = glob.glob(os.path.join(folder_path, '*'))

    # 根据文件的修改时间对文件进行排序
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(x))

    # 逐个重命名文件，赋予递增的序号作为新的文件名
    for index, file_path in enumerate(sorted_files):
        file_extension = os.path.splitext(file_path)[1]  # 获取文件扩展名
        new_filename = f"{index + 1:03d}{file_extension}"  # 使用递增的序号作为新的文件名
        new_file_path = os.path.join(folder_path, new_filename)

        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")


if __name__ == "__main__":
    folder_path = "H:\BaiduNetdiskDownload"  # 替换为你的文件夹路径
    rename_files_by_time(folder_path)
