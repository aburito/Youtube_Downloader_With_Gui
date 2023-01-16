import os.path
import time
from tkinter import *
from tkinter import ttk
import pytube as pt
from pytube.cli import on_progress
import sys
import tkinter.messagebox

window = Tk()
url_var = StringVar(window)


def onClick(name):
    strings = f"Download started for {name}. If the window goes grey, that's okay it'll keep downloading."
    tkinter.messagebox.showinfo('Starting Download', strings)


def FinishedDownload(nameOfVideo):
    top = Toplevel()

    label = Label(top, text= f'Your download of {nameOfVideo} is complete.')
    label.pack()
    top.after(20000, quit())
    top.mainloop()


def DownloadVideo():
    yt = pt.YouTube(url_var.get(), on_progress_callback=on_progress)

    title = yt.title + '.mp4'
    video = yt.streams.get_highest_resolution()
    title = title.replace('?','')
    title = title.replace('/','')
    titleMinusMP4 = title[:-4]
    onClick(titleMinusMP4)
    path = "C:/Users/drochette/PycharmProjects/Youtube_Downloader/Videos/" + title
    print(titleMinusMP4)
    video.download("./Videos")
    flag = True
    x = 0
    while flag:
        if os.path.exists(path):
            flag = False
            FinishedDownload(titleMinusMP4)

        else:
            print(x)
            x = x + 5
            time.sleep(5)


def MakeWindow():
    window.title("Youtube Downloader")

    entry = tkinter.Entry(window, textvariable=url_var, width=100)
    entry.pack()

    button = ttk.Button(window, text='Download', width=100, command=DownloadVideo)
    button.pack()

    window.mainloop()


if len(sys.argv) == 2:
    url = sys.argv[1]
    DownloadVideo()
else:
    MakeWindow()
    url = str(input("Please Enter Video URL: "))
    print(url)
#
