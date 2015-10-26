import tkinter

def getText(text):
    from tkinter.messagebox import showinfo
    showinfo(title='popup', message='Hoi '+text)

window = tkinter.Tk()
window.minsize(150,50)
tk = tkinter
label = tk.Label(window, text='Vul uw email adres in:')
label.pack()
email = tk.Entry(window)
email.pack()
button = tk.Button(window, text='Enter',command=(lambda: getText(email.get())))
button.pack()
window.mainloop()