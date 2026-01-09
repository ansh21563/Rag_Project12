import requests
import os

url = "https://platform.qubrid.com/api/v1/audio/transcriptions"

headers = {
    # "Authorization": "k_9237d83043b9.i2ImCYGghJGVCf5Bg1qVKXt23637TJ0kQ1bMB-anQLwy-wJPFgfEoA"
}

audio_path = "audios/1_MIT6_S897S19_lec01_300k.mp4.mp3"

files = {
    "file": open(audio_path, "rb")
}

data = {
    "model": "openai/whisper-large-v3"
}

response = requests.post(url, headers=headers, files=files, data=data)

print("Status:", response.status_code)
print("Response:", response.text)