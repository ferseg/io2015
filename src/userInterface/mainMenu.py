from tkinter import Tk, Label, Button
from fileChooser import *

class mainMenu:
    def __init__(self):
        self.master = Tk()
        self.master.title("Investigación de Operaciones")
        self.fileChooser = fileChooser()
        
        self.label = Label(self.master, text="This is our first GUI!")
        self.label.pack()

        self.LP_button = Button(self.master, text="Programación Lineal",
                                   command=self.open_fileChooser)
        self.LP_button.pack()

        self.close_button = Button(self.master, text="Cerrar",
                                   command=self.destroy_window)
        self.close_button.pack()

        self.master.mainloop()

    def open_fileChooser(self):
        self.fileChooser.show_fileChooser()
        print(self.fileChooser.get_fileName())

    def destroy_window(self):
        self.master.destroy()

my_gui = mainMenu()



