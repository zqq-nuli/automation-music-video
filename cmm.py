import os
# 用来将音频重命名

def rename_files(directory):
    # 获取目录下的所有文件
    files = os.listdir(directory)
    files.sort()  # 按照文件名排序

    # 遍历文件并重命名
    for i, file_name in enumerate(files):
        # 构建新的文件名
        new_name = str(i + 1) + os.path.splitext(file_name)[1]
        # 构建文件的完整路径
        old_path = os.path.join(directory, file_name)
        new_path = os.path.join(directory, new_name)
        # 重命名文件
        os.rename(old_path, new_path)
        print(f'Renamed: {file_name} -> {new_name}')


# 指定音频文件所在的目录
music_dir = './musics'

# 调用函数进行重命名
rename_files(music_dir)
