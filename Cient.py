import socket
from threading import Thread
from tkinter import *
from tkinter import ttk

from playsound import playsound
import pygame
from pygame import mixer

import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path




PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

for file in os.listdir('shared_files'):
    filename = os.fsdecode(file)
    listbox.insert(song_selected, filename)
    song_counter = song_counter + 1


def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infolabel.configure(text="Now Playing: " +song_selected)
    else:
        infolabel.configure(text="")


def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infolabel.configure(text="")
    

def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry("300*300")
    window.configure(bg = 'Lightskyblue')
    
    global listbox
    global infolabel
    global selectlabel
    
    selectlabel = Label(window, text= "Select Song",bg='LightSkyBlue',font = ("Calibri",0))
    selectlabel.place(x=2, y=1)
    
    listbox = Listbox(window, height = 10,width = 39, activestyle= 'dotbox',bg='LightSkyBlue',borderwidth=2, font =("Calibri",10))
    listbox.place(x=10, y=10)
    
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight= 1, relx= 1)
    scrollbar1.config(command= listbox.yview)
    
    PlayButton = Button(window,text = "Play",width=10,bd=1,bg='SkyBlue',font = ("Calibri",10),command=play)
    PlayButton.place(x=30,y=200)
    
    Stop =Button(window, text="Stop",width=10,bd=1,bg= 'SkyBlue',font = ("Calibri",10))
    Stop.place(x=200,y=200)
    
    Upload=Button(window, text="Upload", width=10,bd=1,bg='SkyBlue',font= ("Calibri",10))
    Upload.place(x=200, y=200)
    
    Download=Button(window,text="Download",width=10, bd=1,bg='SkyBlue',font= ("Calibri",10))
    Download.place(x=200,y=250)
    
    infolabel = Label(window, text= "", fg="blue", font = ("Calibri",0))
    infolabel.place(x=4, y=200)
    window.mainloop()
    
    

        
 
    
    
    

       



def setup():
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.secket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    musicWindow()
setup()


