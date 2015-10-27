import tkinter
import Thuisbioscoop as TB
# from PIL import ImageTk, Image



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

photo = tk.PhotoImage(file="deze.gif") #werkt nog niet, weet niet waarom - werkt wel
w = tk.Label(window, image=photo)
# w.place(x=0, y=0, relwidth=1, relheight=1) #voor het geval je het als achtergrond wil plaatsen, w.pack() moet uit staan


label = tk.Label(window, text='Username:', fg="white", bg="black")

username = tk.Entry(window, bg="white")

passlabel = tk.Label(window, text="Password:", fg="white", bg="black")

password = tk.Entry(window, bg="white", show="*")

bsignin = tk.Button(window, text='Sign in',command=(lambda: logIn()))

attemptsLeft = tk.Label(window, text="Attempts left: 5", fg="white", bg="black")

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