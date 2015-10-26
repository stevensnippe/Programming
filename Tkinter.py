import tkinter
# from PIL import ImageTk, Image


def getText(text, password):
    from tkinter.messagebox import showinfo
    showinfo(title='popup', message='Hoi '+text)


def newuser():
    window.destroy()
    newuserwindow = tkinter.Tk()
    newuserwindow.title("Flexchill")
    newuserwindow.wm_iconbitmap("favicon.ico")  #de logo van het programma
    newuserwindow.configure(background="black")

    newuserwindow.mainloop()


window = tkinter.Tk()
window.geometry("300x300")
window.title("Flexchill")
window.wm_iconbitmap("favicon.ico")  #de logo van het programma
window.configure(background="black")

tk = tkinter

photo = tk.PhotoImage(file="deze.gif") #werkt nog niet, weet niet waarom
w = tk.Label(window, image=photo)
# w.place(x=0, y=0, relwidth=1, relheight=1) #voor het geval je het als achtergrond wil plaatsen, w.pack() moet uit staan


label = tk.Label(window, text='Email:', fg="white", bg="black")

email = tk.Entry(window)

passlabel = tk.Label(window, text="Password:", fg="white", bg="black")

password = tk.Entry(window)

bsignin = tk.Button(window, text='Sign in',command=(lambda: getText(email.get(), password.get())))

bsignup = tk.Button(window, text="Sign up", command=(lambda: newuser()))
#hieronder staat de volgorde van de programma's
w.pack(side="top")
label.pack()
email.pack()
passlabel.pack()
password.pack()
bsignin.pack()
bsignup.pack(side="right")
window.mainloop()