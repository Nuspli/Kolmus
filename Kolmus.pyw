from tkinter import Tk, Label, PhotoImage
from random import randint
from requests import get
from PIL import Image as im
import io, sys, time
from playsound import playsound
from multiprocessing import Process
import webbrowser
from pathlib import Path

image_urls =["https://bot.to/wp-content/uploads/2020/09/antirickroll_5f6fcaafddcd9.png",
             "https://styles.redditmedia.com/t5_3d3rqx/styles/communityIcon_j93l74ux7kx51.png?width=256&s=fa2767dae0ab75ef06c6a1a5ca8e4b7b23711c90",
             "https://www.androidfreeware.net/img2/com-PlayCastle-popcat.jpg",
             "https://static.planetminecraft.com/files/resource_media/screenshot/1229/trollface_2964245_thumb.jpg"]

img_names = ["rick.png", "vibe.png", "pop.png", "troll.png"]
titles = ["Never gonna give you up !", "oh no, you've got Kolmus",
          "pOp pOp pOp pOp pOp pOp pOp pOp", "Trolo lolo lo lololo lololo lolololoo"]

for i in range(len(image_urls)):
    image_bytes = io.BytesIO(get(image_urls[i]).content)
    image = im.open(image_bytes).convert("RGB").save(img_names[i])

f = 0

def music():
    webbrowser.open('https://github.com/Nuspli/rickrol/blob/main/rick.mp3?raw=true', autoraise=False)
    time.sleep(3)
    while True:
        playsound(f'{str(Path.home() / "Downloads/rick.mp3")}')


def on_closing(r):
    r.destroy()
    if f == 1:
        root = Tk()
        root.title("")
        root.configure(background='black')
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))
    newWin()
    newWin()

def newWin():
    ran = randint(0, 3)
    rooot = Tk()
    rooot.title(titles[ran])
    rooot.geometry(f'256x256+{randint(0, rooot.winfo_screenwidth() - 256)}+{randint(0, rooot.winfo_screenheight() - 256)}')
    rooot.resizable(False, False)

    rooot.photo = PhotoImage(master=rooot, file=img_names[ran])
    rooot.label = Label(rooot, image=rooot.photo)
    rooot.label.pack()

    rooot.attributes('-toolwindow', True)
    rooot.attributes('-topmost', True)
    rooot.protocol("WM_DELETE_WINDOW", lambda arg=rooot: on_closing(arg))
    global f
    f += 1

rocket = 0

def func1():
    global rocket
    root = Tk()

    root.title("oh no, you've got Kolmus")
    root.geometry(f'256x256+{randint(0, root.winfo_screenwidth() - 256)}+{randint(0, root.winfo_screenheight() - 256)}')
    root.resizable(False, False)
    photo = PhotoImage(file=img_names[1])
    Label(image=photo).pack()

    root.attributes('-toolwindow', True)
    root.attributes('-topmost', True)
    root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))
    global f
    f += 1
    root.mainloop()

    while rocket < sys.maxsize:
        rocket += 1

def func2():
    global rocket
    music()
    while rocket < sys.maxsize:
        rocket += 1

if __name__=='__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()

