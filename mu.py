import os
import subprocess
from moviepy.editor import concatenate_audioclips, AudioFileClip
from tqdm import tqdm
# 用来合成音频

def concatenate_audio(input_dir, output_file):
    audio_files = [f for f in os.listdir(input_dir) if f.endswith('.mp3')]
    audio_clips = [AudioFileClip(os.path.join(input_dir, f))
                   for f in audio_files]

    # 计算进度条的总长度
    total_duration = sum([clip.duration for clip in audio_clips])

    # 使用 tqdm 显示进度条
    with tqdm(total=total_duration, unit='s', ncols=80) as pbar:
        final_clip = concatenate_audioclips(audio_clips)
        final_clip = final_clip.volumex(0.8)  # 降低音量 20%
        final_clip.write_audiofile(output_file)
        pbar.update(total_duration)


# 使用示例
input_dir = '.\\musics'
output_file = '.\\audio.mp3'
concatenate_audio(input_dir, output_file)
