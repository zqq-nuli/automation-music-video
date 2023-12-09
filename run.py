from moviepy.editor import *
from tqdm import tqdm
from moviepy.editor import *


def merge_audio_image(audio_path, image_path, output_path):

    # 设置画面比例和画质
    video_resolution = (1920, 1080)  # 16:9 画质为 1080p

    # 加载音频和图片
    audio = AudioFileClip(audio_path)
    image = ImageClip(image_path).set_duration(audio.duration)

    # 将图片调整为指定画面比例
    image = image.resize(video_resolution)

    # 合成视频
    video = CompositeVideoClip([image.set_audio(audio)])

    # 导出视频
    video.write_videofile(output_path, codec="libx264", fps=24)


# 调用函数进行合成
audio_path = ".\\audio.mp3"
image_path = ".\\out.jpg"
output_path = ".\\result.mp4"

merge_audio_image(audio_path, image_path, output_path)
