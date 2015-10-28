import tkinter
import tkinter.ttk
import tkinter.messagebox
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
    # names = ["kees", "philippe", "dylan"]
    button = {}
    buttonkopen = {}
    TB.schrijf_xml(TB.response)
    TB.films_dict = TB.verwerk_xml()
    filmnamen = TB.print_filmnamen(TB.films_dict)  # filmnamen geeft alle huidige films in list
    print(filmnamen)  # print de list met alle filmnamen
    rij = 0

    for i in filmnamen:  # http://stackoverflow.com/questions/7300041/tkinter-create-labels-and-entrys-dynamically
        lb = tk.Button(filmwindow, text=i + " (bekijk inhoud)", bg=background, activeforeground=activeforegroundbutton,
                       activebackground=activebackgroundbutton,
                       fg=textkleur, command=lambda piet=i: filmdescription(piet))
        button[i] = lb
        # label[i].bind("<Button-1>",command=(lambda filmdescription("a")))   # http://stackoverflow.com/questions/11504571/clickable-tkinter-labels
        # button[i].grid(row=rij, column=0)

        lb2 = tk.Button(filmwindow, text=i + " Huren", bg=background, activeforeground=activeforegroundbutton,
                        activebackground=activebackgroundbutton,
                        fg=textkleur, command=lambda piet=i: filmdescription(piet))
        buttonkopen[i] = lb2
        # http://stackoverflow.com/questions/11504571/clickable-tkinter-labels
        # button[i].grid(row=rij, column=1)

    # for i in filmnamen:
        buttonkopen[i].pack()  # TODO: een goede layout op het scherm krijgen (met .grid werkt column argument niet?)
        button[i].pack()
        rij += 1

    filmwindow.mainloop()


def filmdescription(film):
    print("hoi " + str(film))


def login():
    if TB.loginPogingen > 0:
        user = username.get().lower()
        pw = password.get()
        accesgranted = TB.login(user, pw)
        # print(accesgranted)
        if accesgranted is True:
            # bron: http://stackoverflow.com/questions/10817917/how-to-disable-input-to-a-text-widget-but-allow-programatic-input
            print("[DEBUG] accesgranted was gelijk aan: "+str(accesgranted))
            username.destroy()  # destroy window
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
            # TODO: hier de code om naar het volgende scherm te gaan waar films worden gedisplayed (nieuwe def)
            goback(2)  # TODO: wanneer geactiveerd slaat hij de accesgranted screen over
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
                photo.configure(file="blocked.gif")  # kan wel beter dan dit maar het idee is er
            return False
    else:
        warning['text'] = "Too many failed login attempts - wait 5 minutes."
        return False


def createaccount():
    readytowrite = False
    user = ename.get().lower()
    pw = epassword.get()
    email = eemail.get().lower()
    provider = comboprovider.get()
    gender = "M"  # TODO: gender ophalen uit radiobutton

    # velden resetten naar defaultcolor white
    ename['bg'] = "white"
    epassword['bg'] = "white"
    eemail['bg'] = "white"
    # comboprovider['bg'] = background

    ingebruik = TB.createLogin(user, pw, email, provider, gender, False)
    # ^SCHRIJFT NIET -- laatste parameter geeft aan alleen data ophalen
    print("login: "+user+"\n", "pw: "+pw+"\n", "email: "+email+"\n", "provider: "+provider+"\n", "ingebruik: "+str(ingebruik)) # , gender --- hoe haal ik info van radiobutton @Debug

    if ingebruik is False:
        readytowrite = True

    if ("." and "@" not in email):
        eemail['bg'] = "red"
        readytowrite = False

    if ingebruik is True:  # ingebruik returnt inUse van createLogin
        ename['bg'] = "red"
        readytowrite = False
        # TODO: Errortextlabel + verkeerde input roodmaken

    if ingebruik is False and readytowrite is True:
        TB.createLogin(user, pw, email, provider, gender, True)  # True dus schrijven naar login.csv
        ingebruik = True
        print("DEBUG: Account created - gender: "+str(gender))
        goback(1)
        # print("test"+radiogender1.selection_get())
        # TODO: maak redirect window naar login + errors uit goback(1) halen
    return ingebruik


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

    # g = tk.StringVar(g)

    lemail = tk.Label(newuserwindow, text="Email:", fg=textkleur, bg=background)
    global eemail
    eemail = tk.Entry(newuserwindow)

    lgender = tk.Label(newuserwindow, text="Gender:", fg=textkleur, bg=background)
    global radiogender1
    radiogender1 = tk.Radiobutton(newuserwindow, text="Male",
                                  padx=20, variable=g, value="Male", fg=textkleur, bg=background)
    global radiogender2
    radiogender2 = tk.Radiobutton(newuserwindow, text="Female",
                                  padx=20, variable=g, value="Female", fg=textkleur, bg=background)

    lname = tk.Label(newuserwindow, text="Username:", fg=textkleur, bg=background)
    global ename
    ename = tk.Entry(newuserwindow)

    lpassword = tk.Label(newuserwindow, text="Password:", fg=textkleur, bg=background)
    global epassword
    epassword = tk.Entry(newuserwindow, show="*")

    lprovider = tk.Label(newuserwindow, text="Provider", fg=textkleur, bg=background)
    global comboprovider
    comboprovider = tk.ttk.Combobox(newuserwindow, values=["", "kpn", "ziggo", "fox", "xs4all"])

    makeaccount = tk.Button(newuserwindow, bg=activebackgroundbutton, fg=activeforegroundbutton,
                            activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton,
                            highlightcolor=highlightbuttoncolorthingy,
                            text="Make Account", command=(lambda: createaccount()))
    gobackwindow = tk.Button(newuserwindow, text="Back", bg=activebackgroundbutton, fg=activeforegroundbutton,
                             activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton,
                             highlightcolor=highlightbuttoncolorthingy,
                             command=(lambda: goback(1)))  # werkt niet, geeft errors (zie functie goback(a))

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
    # TODO: defaultcloseoperation (stoppen met runnen bij kruisje)
    window.geometry("310x300")
    window.title("Chill-Flix")
    window.wm_iconbitmap("favicon.ico")  # de logo van het programma
    window.configure(background=background)
    global photo
    photo = tk.PhotoImage(file="deze.gif")
    w = tk.Label(window, image=photo, borderwidth="0")
    w.image = photo
    global label
    label = tk.Label(window, text='Username:', fg=textkleur, bg=background)
    global username
    username = tk.Entry(window)
    global passlabel
    passlabel = tk.Label(window, text="Password:", fg=textkleur, bg=background)
    global password
    password = tk.Entry(window, show="*")
    global bsignin
    bsignin = tk.Button(window, text='Sign in', bg=activebackgroundbutton, fg=activeforegroundbutton,
                        activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton,
                        highlightcolor=highlightbuttoncolorthingy, command=(lambda: login()))
    global attemptsLeft
    attemptsLeft = tk.Label(window, text="Attempts left: 5", fg="white", bg=background)
    global warning
    warning = tk.Label(window, text="", fg="red", bg=background)
    global bsignup
    bsignup = tk.Button(window, text="Sign up", bg=activebackgroundbutton, fg=activeforegroundbutton,
                        activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton,
                        highlightcolor=highlightbuttoncolorthingy, command=(lambda: newuser()))

    baanvoerder = tk.Button(window, text="Aanvoerder?", bg=activebackgroundbutton, fg=activeforegroundbutton,
                            activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton,
                            highlightcolor=highlightbuttoncolorthingy, command=(lambda: providerscreen()))
    bquit = tk.Button(window, text="Quit", bg=activebackgroundbutton, fg=activeforegroundbutton,
                      activebackground=activebackgroundbutton, activeforeground=activeforegroundbutton,
                      highlightcolor=highlightbuttoncolorthingy,
                      command=(lambda: rommel.destroy() and window.destroy()))
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
    baanvoerder.pack(side="left")
    bquit.pack(side="bottom")
    window.mainloop()


def providerscreen():
    window.destroy()
    rommel.destroy()
    provscreen = tk.Tk()
    provscreen.geometry("310x300")
    provscreen.title("Chill-Flix")
    provscreen.wm_iconbitmap("favicon.ico")  # de logo van het programma
    provscreen.configure(background=background)

    button = {}
    TB.schrijf_xml(TB.response)
    TB.films_dict = TB.verwerk_xml()
    filmnamen = TB.print_filmnamen(TB.films_dict)  # filmnamen geeft alle huidige films in list
    print(filmnamen)  # print de list met alle filmnamen
    rij = 0

    for i in filmnamen:  # http://stackoverflow.com/questions/7300041/tkinter-create-labels-and-entrys-dynamically
        lb = tk.Button(provscreen, text=i, bg=background, fg=textkleur, activeforeground=activeforegroundbutton,
                       activebackground=activebackgroundbutton, command=lambda piet=i: huurdersfilm(piet))
        button[i] = lb
    # button[i].grid(row=rij, column=0)

# for i in filmnamen:
        button[i].pack()
        rij += 1

    provscreen.mainloop()


def huurdersfilm(film):
    tk.messagebox.showinfo(film, film + ":\n" + "")  # TODO: de users van de bijbehorende film als tekst laten zien
menu()