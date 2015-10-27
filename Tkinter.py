import tkinter
import Thuisbioscoop as TB
# from PIL import ImageTk, Image



def logIn():
    user = username.get()
    pw = password.get()
    accesGranted = TB.login(user, pw)
    print(accesGranted)
    if accesGranted == True:
        print("ja")
        #hier de code om naar het volgende scherm te gaan waar films worden gedisplayed
        return True
    else:
        TB.loginPogingen -= 1
        attemptsLeft['text'] = "Attempts left: "+str(TB.loginPogingen)
        warning['text'] = "Login failed"
        return False




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


label = tk.Label(window, text='Username:', fg="white", bg="black")

username = tk.Entry(window)

passlabel = tk.Label(window, text="Password:", fg="white", bg="black")

password = tk.Entry(window)

bsignin = tk.Button(window, text='Sign in',command=(lambda: logIn()))

attemptsLeft = tk.Label(window, text="Attempts left: 3", fg="white", bg="black")

warning = tk.Label(window, text="", fg="red", bg="black")

bsignup = tk.Button(window, text="Sign up", command=(lambda: newuser()))
#hieronder staat de volgorde van de programma's
w.pack(side="top")
label.pack()
username.pack()
passlabel.pack()
password.pack()
bsignin.pack()
attemptsLeft.pack()
warning.pack()
bsignup.pack(side="right")
window.mainloop()