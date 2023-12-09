from pydub import AudioSegment
import os
# 用来检查音频


def check_audio_files(input_folder):
    audio_files = [f for f in os.listdir(
        input_folder) if f.endswith('.mp3') or f.endswith('.wav')]

    for file in audio_files:
        file_path = os.path.join(input_folder, file)
        try:
            audio = AudioSegment.from_file(file_path)
            print(f"{file}: OK")
        except Exception as e:
            print(f"{file}: Error - {str(e)}")


# 指定输入文件夹
input_folder = '.\\musics'

# 检查音频文件是否损坏
check_audio_files(input_folder)
