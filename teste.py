from pytube import YouTube
import os

url = "https://www.youtube.com/watch?v=9bZkp7q19f0&ab_channel=officialpsy"

yt = YouTube(url)

### Download no formato MP4 do Youtube ###
video = yt.streams.get_highest_resolution()
video.download()
