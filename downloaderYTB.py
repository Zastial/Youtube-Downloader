from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os

def check_video_url(video_id):
    #checking if the link is a youtbe one
    #not the best way to do it
    if video_id[:32] == "https://www.youtube.com/watch?v=" or video_id[:17] == "https://youtu.be/":
        return True
    return False

def url(xlink):
    yt = YouTube(xlink)

    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    #Searching for the user's download folder destination
    home = os.path.expanduser('~')
    location = os.path.join(home, 'Downloads')

    #Starting download
    ys.download(location)


def application():
    #Creation of the window
    window = Tk()
    window.title("Youtube Video Downloader")
    window.geometry("500x200")

    #Top Part = Link
    urlvideo = Label(window,text="Whats is the link of the video : ", font=("Arial Bold", 10))
    urlvideo.grid(column=0, row=0)

    texturl = Entry(window)
    texturl.grid(column=1, row=0)

    #Bottom Part = Informations
    labeltitle = Label(window,text="Titre : ", font=("Arial Bold", 10), anchor='w')
    labeltitle.grid(column=0, row=1)
    labelauthor = Label(window,text="Author : ", font=("Arial Bold", 10), anchor='w')
    labelauthor.grid(column=0, row=2)
    labelviews = Label(window,text="Views : ", font=("Arial Bold", 10), anchor='w')
    labelviews.grid(column=0, row=3)
    labellength = Label(window,text="Length : ", font=("Arial Bold", 10), anchor='w')
    labellength.grid(column=0, row=4)

    labelvide = Label(window,text=" ", font=("Arial Bold", 10), anchor='w')
    labelvide.grid(column=0, row=5)

    labeldownloaded = Label(window,text="", font=("Arial Bold", 10), anchor='w')
    labeldownloaded.grid(column=0, row=6)
    
    #Function which recognize when the button is clicked and update the bottom part
    def clicked():
        x = texturl.get()
        if (check_video_url(x) == False):
            messagebox.showerror("Error link", "PLease enter a valid link")
            texturl.delete(0,"end")
        elif (check_video_url(x) == True):
            yt = YouTube(x)
            labeltitle.config(text = f'Titre : {yt.title}')
            labelauthor.config(text = f'Rating : {yt.author}')
            labelviews.config(text = f'Views : {yt.views}')
            labellength.config(text = f'Length : {yt.length} s')
            labeldownloaded.config(text = "Download completed !!")
            url(x)

    #Button that allows the function 'url' to download the video from the link
    btnRead= Button(window, height=1, width=10, text="Valid", command = clicked)
    btnRead.grid(column=3, row=0)
    
    window.mainloop()

if __name__ == "__main__":
    y = application()
    