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
frame_1 = tk.Frame()
frame_2 = tk.Frame()
frame_3 = tk.Frame(master = frame_1)
frame_4 = tk.Frame(master = frame_1)
frame_5 = tk.Frame(master = frame_1)

#CARGAR CANCIÓN
def Cargar():
   
    playlist = filedialog.askopenfilenames(filetypes=[("Archivos MP3", "*.mp3")])
    mixer.init()
    mixer.music.load(playlist[track])


#BARRA DE VOLUMEN
def barra_volumen(val):
    volumen = int(val) / 100
    pygame.mixer.music.set_volume(volumen)

escala = tk.Scale(label='Vol', from_=0, to=100, orient='vertical' , command= barra_volumen,master= frame_2)
escala.set(70)



#REPRODUCIR CANCIÓN
def Reproducir():
    mixer.music.play()

#PARAR CANCIÓN
def Stop():
    mixer.music.stop()

#PAUSAR CANCIÓN
def Pausar():
    mixer.music.pause()


#BOTONES DE LAS FUNCIONES 
#BOTON REPRODUCCIÓN
Boton_Reproducir = tk.Button(text = 'Play', command = Reproducir, master = frame_3) 
Boton_Reproducir.pack()

#BOTÓN STOP
Boton_Stop = tk.Button(text = 'Stop', command = Stop,master= frame_4)
Boton_Stop.pack()

#BOTON PAUSAR
Boton_Pausar = tk.Button (text = 'Pause', command = Pausar, master = frame_5)
Boton_Pausar.pack()


#BOTÓN CARGAR
Boton_Cargar = tk.Button(text = 'Cargar Canción', command = Cargar, master = frame_1)
Boton_Cargar.pack()

escala.pack()

#FRAMES
frame_1.pack(fill=tk.Y, side=tk.LEFT)
frame_2.pack(fill=tk.Y, side=tk.RIGHT)
frame_3.pack(fill=tk.Y, side=tk.RIGHT)
frame_4.pack(fill=tk.Y, side=tk.LEFT)
frame_5.pack(fill=tk.Y, side=tk.TOP)

window.mainloop()