from pytube import YouTube
import moviepy.editor as mp

def youtube_download(url):
    # creating YouTube object
    yt = YouTube(url) 

    # accessing audio streams of YouTube obj.(first one, more available)
    stream = yt.streams.filter().first()
    # downloading a video would be: stream = yt.streams.first() 

    # download into working directory
    path = stream.download()

    # converting to mp3
    clip = mp.VideoFileClip(path)
    clip.audio.write_audiofile('audio.mp3')
    # Getting some basic information
    info = {}
    info['title'] = yt.title
    info['keywords'] = yt.keywords
    return info