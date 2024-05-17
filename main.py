#REPRODUCTOR DE MÚSICA - by TheHlb100
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame
from pygame import mixer
import pathlib

window = tk.Tk()
Título = tk.Label(text = 'Reproductor de música - TheHlb100', bg = 'Blue', fg = 'White')
Título.pack()
track = 0

#CARGAR CANCIÓN
def Cargar():
   
    playlist = filedialog.askopenfilenames(filetypes=[("Archivos MP3", "*.mp3")])
    mixer.init()
    mixer.music.load(playlist[track])

#REPRODUCIR CANCIÓN
def Reproducir():
    
    mixer.music.set_volume(0.7)
    mixer.music.play()

def Stop():
    mixer.music.stop()


#BOTONES DE LAS FUNCIONES 
Boton_Reproducir = ttk.Button(text = 'Play', command = Reproducir)
Boton_Reproducir.pack()

Boton_Stop = ttk.Button(text = 'Stop', command = Stop)
Boton_Stop.pack()

Boton_Cargar = ttk.Button(text = 'Cargar Canción', command = Cargar)
Boton_Cargar.pack()



   
window.mainloop()