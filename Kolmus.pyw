import io, sys, time, os
from tkinter import Tk, Label, PhotoImage, Toplevel
from random import randint
from requests import get
from PIL import Image as im
from playsound import playsound
from multiprocessing import Process
import webbrowser
from pathlib import Path
from keyboard import block_key, unblock_key

windows_to_close = 10

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
    if Path(Path.home() / "Downloads/rick.mp3").is_file() == False:
        webbrowser.open('https://github.com/Nuspli/rickrol/blob/main/rick.mp3?raw=true', autoraise=False)
        time.sleep(5)
    while True:
        playsound(Path.home() / "Downloads/rick.mp3")
        if p1.is_alive() == False:
            sys.exit()


def on_closing(r):

    r.destroy()
    if f == 2*windows_to_close:
        for m in range(150):
            unblock_key(m)
            sys.exit()
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

    roooot = Tk()
    roooot.title("")
    roooot.configure(background='black')
    roooot.geometry(f'{roooot.winfo_screenwidth()}x{roooot.winfo_screenheight()}+0+0')
    roooot.overrideredirect(True)
    root = Tk()

    root.title("close all windows to free your keyboard xD")
    root.geometry(f'256x256+{randint(0, root.winfo_screenwidth() - 256)}+{randint(0, root.winfo_screenheight() - 256)}')
    root.resizable(False, False)
    photo = PhotoImage(master=root, file=img_names[1])
    Label(root, image=photo).pack()

    root.attributes('-toolwindow', True)
    root.attributes('-topmost', True)
    root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))

    for m in range(150):
        block_key(m)
    root.mainloop()

    roooot.after(100, root.mainloop())
    roooot.mainloop()

    while rocket < sys.maxsize:
        rocket += 1

def func2():
    global rocket
    music()
    while rocket < sys.maxsize:
        rocket += 1

if __name__=='__main__':
    p2 = Process(target=func2)
    p2.start()
    p1 = Process(target=func1)
    p1.start()
