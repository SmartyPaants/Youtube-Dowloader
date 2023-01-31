from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

def select_path():
    # Allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    # Get user path
    get_link = link.get()
    # Get selected path
    user_path = path_label.cget("text")
    root.title('Downloading...')
    # Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # Move file to selected directory
    shutil.move(mp4_video, user_path)
    root.title('Download Complete! Download Another File...')
    linkl.config(text="Enter another URL for download: ")

root = Tk()
title = root.title('Youtube Video Downloader')
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Loading Image
img = PhotoImage(file="yt.png")
img = img.subsample(3, 3)
canvas.create_image(250, 50, image=img)

# Heading
heading = Label(root, text="Youtube Video Dowloader", font=("Arial", 20, 'bold'))
canvas.create_window(250, 120, window=heading)

# Link
linkl = Label(root, text="Enter link for download below: ", font=("Microsoft yahie UI Light", 14, 'bold'))
canvas.create_window(260, 175, window=linkl)

linll = Label(root, text="Link :-> ", font=("Microsoft yahie UI Light", 14, 'bold'))
canvas.create_window(75, 200, window=linll)

link = Entry(root, fg='black', bd=1, width=35, bg='light yellow', font=("Microsoft yahie UI Light", 12))
canvas.create_window(275, 200, window=link)

# Select Path for saving the file
path_label = Label(root, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(root, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
# Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# Select Button
select_btn =  Button(root, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
canvas.create_window(250, 330, window=select_btn)

# Download Button
download = Button(root, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
canvas.create_window(250,390, window=download)

root.mainloop()