def filmscreen():
    filmwindow = tkinter.Tk()
    filmwindow.geometry(windowsize)
    filmwindow.title("Chill-Flix")
    filmwindow.wm_iconbitmap("favicon.ico")  # de logo van het programma
    filmwindow.configure(background=background)
    names = ["kees", "philippe", "dylan"]
    label = {}
    for i in names: # http://stackoverflow.com/questions/7300041/tkinter-create-labels-and-entrys-dynamically
        lb = tk.Label(filmwindow, text=i, bg=background, fg=textkleur)
        label[i] = lb
        # label[i].bind("<Button-1>",command=(lambda filmdescription("a")))   # http://stackoverflow.com/questions/11504571/clickable-tkinter-labels   hoort filmdescription op te roepen wanneer je drukt op de label
        label[i].pack()


    filmwindow.mainloop()


def filmdescription(film):
    print("hoi")