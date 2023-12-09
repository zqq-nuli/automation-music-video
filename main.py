import requests
import os
import json
from tqdm import tqdm
# 用来下载音频

# 读取 JSON 文件
with open('data.json', 'r') as file:
    json_data = file.read()

# 解析 JSON 数据为 Python 对象
# data = json.loads(json_data)
# 给定的音乐数组对象
music_array = json.loads(json_data)

# 设置保存音乐的文件夹
save_folder = "./musics"

# 确保保存文件的文件夹存在
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 循环遍历音乐数组对象并下载音乐
for music in music_array:
    # 获取音乐文件名（使用 title 字段的值）
    file_name = music["title"] + ".mp3"

    # 获取音乐文件链接
    url = music["preview_url"]

    # 发起请求并保存文件
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    # 进度条初始化
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)
    
    with open(os.path.join(save_folder, file_name), 'wb') as file:
        for data in response.iter_content(chunk_size=1024):
            # 更新进度条
            progress_bar.update(len(data))
            
            # 写入文件
            file.write(data)
    
    # 关闭进度条
    progress_bar.close()

    print(f"{file_name} 下载完成")
