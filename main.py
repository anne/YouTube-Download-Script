import youtube_dl
import logging
import sys
import os
import json




def main():
    print("Running YouTube Download Script")
    print(sys.argv)
    if len(sys.argv) > 1:
        download_youtube_video(sys.argv[1])
    return



def download_youtube_video(youtube_url_passed_in):
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
