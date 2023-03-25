from pytube import YouTube

link = input('https://youtu.be/GtvUxXyFoMw')

yt = YouTube(link)
yt.streams.first().download()

print('download', link)