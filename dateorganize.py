import pathlib
import os
import datetime
from time import strftime
files = []
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
        os.rename(x,fm_year+"/"+fm_month+"/"+fm_day+"/"+x)
        print("Successfully Moved " + x)
    except:
        print("Failed to move a file.")
