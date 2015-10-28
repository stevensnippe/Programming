import tkinter
import tkinter.ttk
import Thuisbioscoop as TB
import time
# import animateGifs as aG
# from PIL import ImageTk, Image
g=0
tk = tkinter

global background
background = "#153341"
global textkleur
textkleur = "#51dfd4"
global windowsize
windowsize = "350x300"
global titelimage
titleimage = "deze.gif"
global activebackgroundbutton
activebackgroundbutton = "#245A69"
global activeforegroundbutton
activeforegroundbutton = "#48ABAA"
global highlightbuttoncolorthingy
highlightbuttoncolorthingy = "#6B99A0"


def filmscreen():
    filmwindow = tkinter.Tk()
    filmwindow.geometry(windowsize)
    filmwindow.title("Chill-Flix")
    filmwindow.wm_iconbitmap("favicon.ico")  # de logo van het programma
    filmwindow.configure(background=background)
    names = ["kees", "philippe", "dylan"]
    button = {}
    for i in names: # http://stackoverflow.com/questions/7300041/tkinter-create-labels-and-entrys-dynamically
        lb = tk.Button(filmwindow, text=i, command=lambda piet=i:filmdescription(piet), bg=background, fg=textkleur)
        button[i] = lb
        # label[i].bind("<Button-1>",command=(lambda filmdescription("a")))   # http://stackoverflow.com/questions/11504571/clickable-tkinter-labels   hoort filmdescription op te roepen wanneer je drukt op de label
        button[i].pack()

    filmwindow.mainloop()


def filmdescription(film):
    print("hoi" + film)

filmscreen()
TB.schrijf_xml(TB.response)
TB.films_dict = TB.verwerk_xml()
filmNamen = TB.print_filmnamen(TB.films_dict) # filmNamen geeft alle huidige films in list
print(filmNamen) # print de list met alle filmnamen
for i in filmNamen: # print films 1 voor 1
    print(str(i)) # TODO: hier code om in tkinter te zetten