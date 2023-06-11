from pytube import YouTube
import os

url = "https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy"

yt = YoutTube(url)


### Download no formato MP4 do Youtube ###
video = yt.streams.get_hightest_resolution()
video.download()

### Download Formato MP3 do Youtube ###
audio = yt.streams.filter(only_audio=True).first()
out_file = audio.download()
### Salvando o arquivo em mp3 ###
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
### Retorno para Confirmação ###
print(yt.title + " Download executado com sucesso")
