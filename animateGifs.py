from threading import Thread
from Tkinter import *
import time
import os

# Bron: https://www.youtube.com/watch?v=IeYHqn5LFmM
class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.pack(fill=BOTH)
        tk.protocol("WM_DELETE_WINDOW", self.close)
        self.num = 0
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, bd=0)
        self.label.pack()
        Thread(target=self.animate).start()

    def animate(self):
        while True:
            try:
                time.sleep(0.04)
                img = PhotoImage(file="loading.gif", format="gif - {}".format(self.num))
                self.label.config(image=img)
                self.label.image=img
                self.num += 1
            except: self.num = 0

    def close(self):
        os._exit(0)

    """
    def animate(self):
        if self._image_id is None:
            self._image_id = self.display.create_image("loading.gif")
        else:
            self.itemconfig(self._image_id, image="newimg")
        self.display.after(self.gif["delay"], self.animate)
    """

#root = Tk()
#app = Application(root)
#root.mainloop()