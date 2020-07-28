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
    # detect files in current directory
    dirs = os.listdir(".")
    file_list = []
    for file in dirs:
        file_list.append(str(file))
    print(file_list)
    # download youtube video
    youtube_url = "https://www.youtube.com/watch?v=ZrsYIthVY-Y"
    youtube_url_array = [youtube_url]
    ydl_opts = {
        'outtmpl': "%(id)s.%(ext)s",
        'forcejson' : True,
        'writeinfojson' : True,
        'write_all_thumbnails' : True,
        'writesubtitles' : True,
        'writeautomaticsub' : True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(youtube_url_array)
    # get new file list
    dirs = os.listdir(".")
    new_file_list = []
    for file in dirs:
        new_file_list.append(str(file))
    print(new_file_list)
    # remove files that were in the list previously
    for old_item in file_list:
        new_file_list.remove(old_item)
    # now iterate through the new files list
    for new_file in new_file_list:
        os.system("gsutil cp " + str(new_file) + " gs://farmtwitter.appspot.com/")
    

    
    
print(__name__)
if __name__ == "__main__":
    main()    
