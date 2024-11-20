import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("music spiller")#navn på pygame
canvas.geometry("600x800") #størelse pygamet
canvas.config(bg = "black")#bagrunn mygamet

rootpath = "C:\\Users\samue\OneDrive - Buskerud fylkeskommune\programfag\yff\musikk yff uke 45"#rootpath til en mappe med sangene som jeg brukte
pattern = "*.mp3" #gjør så jeg kun leter etter mp3 filer som slutter med mp3

mixer.init()

#def
def select():
    label.config(text= listbox.get("anchor"))#Henter filnavnet til den valgte sangen i listen
    mixer.music.load(rootpath + "//" + listbox.get("anchor"))#Laster den valgte filen fra rootpath 
    mixer.music.play()#starter avspiling av sangen

def stop():
    mixer.music.stop()#Stopper avspilling av musikken.
    listbox.select_clear("active")#Fjerner markeringen fra den aktive sangen i listen.


    
    #hvis knapen viser "pause" når jeg trykker play bytter knappen text til play 
def pause_song(): 
    if pausebutton["text"] == "pause":
        mixer.music.pause()
        pausebutton["text"] = "play"
    else:
        mixer.music.unpause()
        pausebutton["text"] = "pause"


    
#oppreter en box med filene i en liste
listbox = tk.Listbox(fg= "cyan", bg= "black", width= 100, font= ("bold", 14))
listbox.pack( pady= 15)

label = tk.Label(fg= "cyan", bg= "black", width= 100, font= ("bold", 14))
label.pack(padx= 15, pady= 15)

#får alle mp3ene fra rootpathen inn i listbox
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert("end", filename)


top =tk.Frame(canvas, bg= "black")
top.pack(pady = 15, anchor = "center")




#stop knapp
stopbutton = tk.Button(canvas, text = "stop", command = stop)
stopbutton.pack(pady = 15, in_ = top, side = "left")

#start knapp
startbutton = tk.Button(canvas, text = "start", command = select) 
startbutton.pack(pady = 15, in_ = top, side = "left")

#pause knapp
pausebutton = tk.Button(canvas, text = "pause", command = pause_song)
pausebutton.pack(pady = 15, in_ = top, side = "left")





canvas.mainloop()

