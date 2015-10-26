import tkinter

def getText(text):
    from tkinter.messagebox import showinfo
    showinfo(title='popup', message='Hoi '+text)

window = tkinter.Tk()
window.geometry("300x300")
window.title("Flexchill")
window.wm_iconbitmap("favicon.ico")  #de logo van het programma

tk = tkinter
label = tk.Label(window, text='Vul uw email adres in:')

email = tk.Entry(window)

button = tk.Button(window, text='Enter',command=(lambda: getText(email.get())))


label.pack()
email.pack()
button.pack()
window.mainloop()