#This one is for organizing stuff like images and memes, without stuff like pdfs and executables getting mixed in.
import pathlib
import os
import datetime
from time import strftime
files = []
supported = [".jpg", ".png", ".webm", ".jpeg", ".mp4", ".gif"]
lsdir = os.listdir(path=".")
print("Folder File Date Organizer")
for x in lsdir:
    isDir = os.path.isdir(x)
    if isDir is False and x != __file__:
        files.append(x)
for x in files:
    fstat = os.stat(x).st_mtime
    filemtime = datetime.datetime.fromtimestamp(fstat)
    fm_day = filemtime.strftime("%d")
    fm_month = filemtime.strftime("%B")
    fm_year = filemtime.strftime("%Y")
    try:
        if not os.path.exists(fm_year):os.mkdir(fm_year)
        if not os.path.exists(fm_year+"/"+fm_month):os.mkdir(fm_year+"/"+fm_month)
        if not os.path.exists(fm_year+"/"+fm_month+"/"+fm_day):os.mkdir(fm_year+"/"+fm_month+"/"+fm_day)
    except:
        print("Failed to create a folder. Please check permissions.")
        sys.exit()
    try:
        filename, file_extension = os.path.splitext(x)
        if file_extension in supported:
            os.rename(x,fm_year+"/"+fm_month+"/"+fm_day+"/"+x)
            print("Successfully Moved " + x)
    except:
        print("Failed to move a file.")
