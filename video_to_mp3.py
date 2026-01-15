# converts the video to mp3
import os
import subprocess

files=os.listdir("videos")
for file in files:
    # print(file)
    parts = file.split("{}")
    tutorial_number=parts[0]
    file_name = parts[1]
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i",f"videos/{file}",f"audios/{tutorial_number}_{file_name}.mp3" ])