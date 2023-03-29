
import pytube as pt

def run():
    url_input = input("please enter the url:")
    yt = pt.YouTube(url_input)
    t =    yt.streams.filter(only_audio=True,abr='128kbps')
    t[0].download()



