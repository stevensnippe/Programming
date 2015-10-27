import tkinter
# from PIL import ImageTk, Image

tk = tkinter


def gettext(text, password):
    from tkinter.messagebox import showinfo
    showinfo(title='popup', message='Hoi '+text)


def newuser():
    global newuserwindow
    window.destroy()
    rommel.destroy()
    newuserwindow = tkinter.Tk()
    newuserwindow.title("Flexchill")
    newuserwindow.wm_iconbitmap("favicon.ico")  # de logo van het programma
    newuserwindow.configure(background="black")

    lname = tk.Label(newuserwindow, text="Name:", fg="white", bg="black")
    ename = tk.Entry(newuserwindow)

    lemail = tk.Label(newuserwindow, text="Email:", fg="white", bg="black")
    eemail = tk.Entry(newuserwindow)

    lpassword = tk.Label(newuserwindow, text="Password:", fg="white", bg="black")
    epassword = tk.Entry(newuserwindow)

    makeaccount = tk.Button(newuserwindow, text="Make Account")
    gobackwindow = tk.Button(newuserwindow, text="Back", command=(lambda: goback(1)))  # werkt niet, geeft errors (zie functie goback(a))

    lname.pack()
    ename.pack()
    lemail.pack()
    eemail.pack()
    lpassword.pack()
    epassword.pack()
    makeaccount.pack()
    gobackwindow.pack(side="left")
    newuserwindow.mainloop()


def goback(a):
    if a == 1:
        global newuserwindow
        newuserwindow.destroy()
        menu()


def menu():
    """
   Let op! programma sluit pas echt af als je op quit drukt"""
    global window
    global rommel
    rommel = tkinter.Tk()  # houd een tweede scherm tegen
    rommel.withdraw()
    window = tkinter.Toplevel()
    window.geometry("300x300")
    window.title("Flexchill")
    window.wm_iconbitmap("favicon.ico")  # de logo van het programma
    window.configure(background="black")

    photo = tk.PhotoImage(file="deze.gif")
    w = tk.Label(window, image=photo)
    w.image = photo
    # w.place(x=0, y=0, relwidth=1, relheight=1) #voor het geval je het als achtergrond wil plaatsen, w.pack() moet uit staan

    label = tk.Label(window, text='Username:', fg="white", bg="black")

    email = tk.Entry(window)

    passlabel = tk.Label(window, text="Password:", fg="white", bg="black")

    password = tk.Entry(window)

    bsignin = tk.Button(window, text='Sign in', command=(lambda: gettext(email.get(), password.get())))

    bsignup = tk.Button(window, text="Sign up", command=(lambda: newuser()))

    bquit = tk.Button(window, text="Quit", command=(lambda: rommel.destroy() and window.destroy()))
    # hieronder staat de volgorde van de programma's
    w.pack(side="top")
    label.pack()
    email.pack()
    passlabel.pack()
    password.pack()
    bsignin.pack()
    bsignup.pack(side="right")
    bquit.pack(side="bottom")
    window.mainloop()

menu()