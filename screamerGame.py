import os
import ctypes
import time
import pyautogui as pg
import subprocess
import webbrowser
import pygame
from tkinter import *
from PIL import ImageTk, Image
import requests

'''Theres is a simple code of windows screamer!!
You can use it to pranked your friends or improve this code'''


#  Getting size of screen
w, h = pg.size()

# Getting images and sound for screamer
########################################################
r = requests.get("https://images.alphacoders.com/564/564627.jpg")
with open("C:\\bg.jpg", "wb") as file:
    file.write(r.content)

r2 = requests.get("https://avatarfiles.alphacoders.com/916/91624.jpg")
with open("C:\\1.jpg", "wb") as file:
    file.write(r2.content)

r3 = requests.get("https://cdn.pixabay.com/audio/2022/03/10/audio_c3a6b431e4.mp3")
with open("C:\\scream-with-echo-46585.mp3", "wb") as file:
    file.write(r3.content)
##########################################################


# send Message
################################################################
pg.alert(text='let me show you something', title='Hacker', button='OK')

# opening a browser with photos of the specified items
webbrowser.open(
    'https://www.google.com/search?q={{{{ HERE YOUR WORD }}}}&rlz=1C1GGRV_ukUA991UA991&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiSsJCjy4b9AhVNmYsKHTvpBJEQ_AUoAXoECAEQAw&biw=1081&bih=945&dpr=1')

time.sleep(4)

# send Message
pg.alert(text="oh shit you are not supposed to see it", button='ok', title='hacker')
# opening a browser with photos of the specified items
webbrowser.open(
    'https://www.google.com/search?q={{{{ HERE YOUR WORD }}}}&rlz=1C1GGRV_ukUA991UA991&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiSsJCjy4b9AhVNmYsKHTvpBJEQ_AUoAXoECAEQAw&biw=1081&bih=945&dpr=1')

time.sleep(4)
##############################################################

# This command close chrome windows
#Also you can close all windows by useing - os.system("TASKKILL /F /IM *.exe")
os.system("TASKKILL /F /IM chrome.exe")

pg.prompt(text="So, what do you think about that?")

# Connect sound of screams which we parsed
pygame.mixer.init()
def play():
    pygame.mixer.music.load("scream-with-echo-46585.mp3")
    pygame.mixer.music.play(loops=0)

# Tkinter: creating are to pt our screamer img
root = Tk()
root.geometry(f"{w}x{h}")

root.configure(background='black')
root.overrideredirect(True)

#Open img
img = ImageTk.PhotoImage(Image.open("C:\\1.jpg"))

#Dispaing screamer
label = Label(root, image=img, border=0)
label.pack()

# Sound
play()

#This command changes your wallper
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\bg.jpg", 3)

root.after(3600, lambda: root.destroy())
root.mainloop()

# Be careful with this command
# Its turn off your PC
# COMMAND = "Stop-Computer -Force"
# subprocess.run(['powershell', '-command', COMMAND], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)