import tkinter
import tkinter.ttk
import Thuisbioscoop as TB
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


def logIn():
    if TB.loginPogingen > 0:
        user = username.get()
        pw = password.get()
        accesGranted = TB.login(user, pw)
        #print(accesGranted)
        if accesGranted == True: #TODO: image en tekst naar het midden bij succesful login
            print("test")
            username.pack_forget() #hide field
            password.pack_forget()
            bsignin.pack_forget()
            attemptsLeft.pack_forget()
            label.pack_forget()
            passlabel.pack_forget()
            bsignup.pack_forget()
            warning.pack_forget()
            label2 = tk.Label(window, text='Login succesful, u word doorverwezen.', fg="white", bg="black")
            label2.pack()
            #TODO: hier de code om naar het volgende scherm te gaan waar films worden gedisplayed (nieuwe def)
            return True
        else:
            TB.loginPogingen -= 1
            attemptsLeft['text'] = "Attempts left: "+str(TB.loginPogingen)
            warning['text'] = "Login failed, invalid username or password."
            if TB.loginPogingen == 0:
                warning['text'] = "Too many failed login attempts - wait 5 minutes."
                #username['bg'] = "red"
                #password['bg'] = "red"
                username.configure(state="disabled")
                password.configure(state="disabled")
                bsignin.configure(state="disabled")
                photo.configure(file="blocked.gif") #kan wel beter dan dit maar het idee is er
            return False
    else:
        warning['text'] = "Too many failed login attempts - wait 5 minutes."
        return False


def newuser():
    global newuserwindow
    global g
    global v
    window.destroy()
    rommel.destroy()
    newuserwindow = tkinter.Tk()
    newuserwindow.geometry(windowsize)
    newuserwindow.title("Flexchill")
    newuserwindow.wm_iconbitmap("favicon.ico")  # de logo van het programma
    newuserwindow.configure(background=background)

    lname = tk.Label(newuserwindow, text="Name:", fg=textkleur, bg=background)
    ename = tk.Entry(newuserwindow)

    lgender = tk.Label(newuserwindow, text="Gender:", fg=textkleur, bg=background)
    radiogender1 = tk.Radiobutton(newuserwindow, text="Male", padx=20, variable=g, value=1, fg=textkleur, bg=background)
    radiogender2 = tk.Radiobutton(newuserwindow, text="Female", padx=20, variable=g, value=2, fg=textkleur, bg=background)

    lemail = tk.Label(newuserwindow, text="Email:", fg=textkleur, bg=background)
    eemail = tk.Entry(newuserwindow)

    lpassword = tk.Label(newuserwindow, text="Password:", fg=textkleur, bg=background)
    epassword = tk.Entry(newuserwindow)

    lprovider = tk.Label(newuserwindow, text="Provider", fg=textkleur, bg=background)
    comboprovider = tk.ttk.Combobox(newuserwindow, values=["kpn","ziggo","fox","xs4all"])

    makeaccount = tk.Button(newuserwindow, text="Make Account")
    gobackwindow = tk.Button(newuserwindow, text="Back", command=(lambda: goback(1)))  # werkt niet, geeft errors (zie functie goback(a))

    lname.pack()
    ename.pack()
    lgender.pack()
    radiogender1.pack()
    radiogender2.pack()
    lemail.pack()
    eemail.pack()
    lpassword.pack()
    epassword.pack()
    lprovider.pack()
    comboprovider.pack()
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
    #TODO: defaultcloseoperation (stoppen met runnen bij kruisje)
    window.geometry("310x300")
    window.title("Flexchill")
    window.wm_iconbitmap("favicon.ico")  # de logo van het programma
    window.configure(background=background)
    global photo
    photo = tk.PhotoImage(file="deze.gif")
    w = tk.Label(window, image=photo, borderwidth="0")
    w.image = photo
    # w.place(x=0, y=0, relwidth=1, relheight=1) #voor het geval je het als achtergrond wil plaatsen, w.pack() moet uit staan
    global label
    label = tk.Label(window, text='Username:', fg=textkleur, bg=background)
    global username
    username = tk.Entry(window)
    global passlabel
    passlabel = tk.Label(window, text="Password:", fg=textkleur, bg=background)
    global password
    password = tk.Entry(window, show="*")
    global bsignin
    bsignin = tk.Button(window, text='Sign in', command=(lambda: logIn()))
    global attemptsLeft
    attemptsLeft = tk.Label(window, text="Attempts left: 5", fg="white", bg=background)
    global warning
    warning = tk.Label(window, text="", fg="red", bg=background)
    global bsignup
    bsignup = tk.Button(window, text="Sign up", command=(lambda: newuser()))

    bquit = tk.Button(window, text="Quit", command=(lambda: rommel.destroy() and window.destroy()))
    # hieronder staat de volgorde van de programma's
    w.pack(side="top")
    label.pack()
    username.pack()
    passlabel.pack()
    password.pack()
    bsignin.pack()
    attemptsLeft.pack()
    warning.pack()
    bsignup.pack(side="right")
    bquit.pack(side="bottom")
    window.mainloop()

menu()