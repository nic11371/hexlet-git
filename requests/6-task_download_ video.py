import requests
import time


url = 'http://parsinger.ru/video_downloads/videoplayback.mp4'


response = requests.get(url=url, stream=True)

with open('file.mp4', 'wb') as video:
    # file.write(response.content) для небольших видео файлов
    for piece in response.iter_content(chunk_size=100000): # скачивание по кускам. размер куска в байтах
        video.write(piece)