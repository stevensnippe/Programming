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
    label = {}
    for i in names: # http://stackoverflow.com/questions/7300041/tkinter-create-labels-and-entrys-dynamically
        lb = tk.Label(filmwindow, text=i, bg=background, fg=textkleur)
        label[i] = lb
        # label[i].bind("<Button-1>",command=(lambda filmdescription("a")))   # http://stackoverflow.com/questions/11504571/clickable-tkinter-labels
        label[i].pack()


    filmwindow.mainloop()


def filmdescription(film):
    print("hoi")


def logIn():
    if TB.loginPogingen > 0:
        user = username.get().lower()
        pw = password.get()
        accesGranted = TB.login(user, pw)
        # print(accesGranted)
        if accesGranted == True:
            # bron: http://stackoverflow.com/questions/10817917/how-to-disable-input-to-a-text-widget-but-allow-programatic-input
            print("[DEBUG] accesGranted was gelijk aan: "+str(accesGranted))
            username.destroy() #destroy window
            password.destroy()
            bsignin.destroy()
            attemptsLeft.destroy()
            label.destroy()
            passlabel.destroy()
            bsignup.destroy()
            warning.destroy()
            window.configure(background="black")
            label2 = tk.Label(window, text='Login succesful, redirecting.', fg=textkleur, bg="black")
            label2.pack()
            photo2 = tk.PhotoImage(file="loading.gif")
            # TODO:laad alleen eerste frame, is animated GIF
            w = tk.Label(window, image=photo2, borderwidth="0")
            w.image = photo2
            w.pack()
            # time.sleep(2)
            #TODO: hier de code om naar het volgende scherm te gaan waar films worden gedisplayed (nieuwe def)
            #     goback(2)  # TODO: wanneer geactiveerd slaat hij de accesgranted screen over
            return True
        else:
            TB.loginPogingen -= 1
            attemptsLeft['text'] = "Attempts left: "+str(TB.loginPogingen)
            warning['text'] = "Login failed, invalid username or password."
            if TB.loginPogingen == 0:
                warning['text'] = "Too many failed login attempts - wait 5 minutes."
                username.configure(state="disabled")
                password.configure(state="disabled")
                bsignin.configure(state="disabled")
                photo.configure(file="blocked.gif") #kan wel beter dan dit maar het idee is er
            return False
    else:
        warning['text'] = "Too many failed login attempts - wait 5 minutes."
        return False

def createAccount():
    readyToWrite = False
    user = ename.get().lower()
    pw = epassword.get()
    email = eemail.get().lower()
    provider = comboprovider.get()
    gender = "M" # TODO: gender ophalen uit radiobutton

    # velden resetten naar defaultcolor white
    ename['bg'] = "white"
    epassword['bg'] = "white"
    eemail['bg'] = "white"
    #comboprovider['bg'] = background

    inGebruik = TB.createLogin(user, pw, email, provider, gender, False) # SCHRIJFT NIET -- laatste parameter geeft aan alleen data ophalen
    print("login: "+user+"\n", "pw: "+pw+"\n", "email: "+email+"\n", "provider: "+provider+"\n", "ingebruik: "+str(inGebruik)) # , gender --- hoe haal ik info van radiobutton @Debug

    if inGebruik == False:
        readyToWrite = True

    if ("." and "@" not in email):
        eemail['bg'] = "red"
        readyToWrite = False

    if inGebruik == True: # inGebruik returnt inUse van createLogin
        ename['bg'] = "red"
        readyToWrite = False
        # TODO: Errortextlabel + verkeerde input roodmaken

    if inGebruik == False and readyToWrite == True:
        TB.createLogin(user, pw, email, provider, gender, True) # True dus schrijven naar login.csv
        inGebruik = True
        print("DEBUG: Account created - gender: "+str(gender))
        goback(1)
        # print("test"+radiogender1.selection_get())
        # TODO: maak redirect window naar login + errors uit goback(1) halen
    return inGebruik



def newuser():
    global newuserwindow
    global g
    window.destroy()
    rommel.destroy()
    newuserwindow = tkinter.Tk()
    newuserwindow.geometry(windowsize)
    newuserwindow.title("Chill-Flix")
    newuserwindow.wm_iconbitmap("favicon.ico")  # de logo van het programma
    newuserwindow.configure(background=background)

    lname = tk.Label(newuserwindow, text="Username:", fg=textkleur, bg=background)
    global ename
    ename = tk.Entry(newuserwindow)

    # g = tk.StringVar(g)
    lgender = tk.Label(newuserwindow, text="Gender:", fg=textkleur, bg=background)
    global radiogender1
    radiogender1 = tk.Radiobutton(newuserwindow, text="Male", padx=20, variable=g, value="Male", fg=textkleur, bg=background)
    global radiogender2
    radiogender2 = tk.Radiobutton(newuserwindow, text="Female", padx=20, variable=g, value="Female", fg=textkleur, bg=background)

    lemail = tk.Label(newuserwindow, text="Email:", fg=textkleur, bg=background)
    global eemail
    eemail = tk.Entry(newuserwindow)

    lpassword = tk.Label(newuserwindow, text="Password:", fg=textkleur, bg=background)
    global epassword
    epassword = tk.Entry(newuserwindow, show="*")

    lprovider = tk.Label(newuserwindow, text="Provider", fg=textkleur, bg=background)
    global comboprovider
    comboprovider = tk.ttk.Combobox(newuserwindow, values=["","kpn","ziggo","fox","xs4all"])

    makeaccount = tk.Button(newuserwindow, bg=activebackgroundbutton, fg=activeforegroundbutton, activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton, highlightcolor=highlightbuttoncolorthingy, text="Make Account", command=(lambda: createAccount()))
    gobackwindow = tk.Button(newuserwindow, text="Back", bg=activebackgroundbutton, fg=activeforegroundbutton, activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton, highlightcolor=highlightbuttoncolorthingy, command=(lambda: goback(1)))  # werkt niet, geeft errors (zie functie goback(a))


    lemail.pack()
    eemail.pack()
    lgender.pack()
    radiogender1.pack()
    radiogender2.pack()
    lname.pack()
    ename.pack()
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
    if a == 2:
        global window
        window.destroy()
        rommel.destroy()
        filmscreen()



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
    window.title("Chill-Flix")
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
    bsignin = tk.Button(window, text='Sign in', bg=activebackgroundbutton, fg=activeforegroundbutton, activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton, highlightcolor=highlightbuttoncolorthingy, command=(lambda: logIn()))
    global attemptsLeft
    attemptsLeft = tk.Label(window, text="Attempts left: 5", fg="white", bg=background)
    global warning
    warning = tk.Label(window, text="", fg="red", bg=background)
    global bsignup
    bsignup = tk.Button(window, text="Sign up", bg=activebackgroundbutton, fg=activeforegroundbutton, activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton, highlightcolor=highlightbuttoncolorthingy, command=(lambda: newuser()))

    bquit = tk.Button(window, text="Quit", bg=activebackgroundbutton, fg=activeforegroundbutton, activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton, highlightcolor=highlightbuttoncolorthingy, command=(lambda: rommel.destroy() and window.destroy()))
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