import youtube_dl
import logging
import sys
import os
import json




def main():
    print("test")
    print(sys.argv)
    return



def download_youtube_video(request):
    youtube_url = "https://www.youtube.com/watch?v=ZrsYIthVY-Y"
    youtube_url_array = [youtube_url]
    ydl_opts = {
        'outtmpl': "extract.%(ext)s",
        'forcejson' : True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(youtube_url_array)
    dirs = os.listdir(".")
    for file in dirs:
        print(file)
    

    
    
print(__name__)
if __name__ == "__main__":
    main()    
