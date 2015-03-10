import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class fileChooser:
    def _init_(self):
        self.fileName=""
        
    def show_fileChooser(self):
        """

        :Description: Displays the file chooser
        
        """
        Tk().withdraw()
        self.fileName=tkinter.filedialog.askopenfilename()

    def get_fileName(self):
        """

        :return: The file path, it could be an empty string
        
        """
        return self.fileName

#example
test=fileChooser()
test.show_fileChooser()
print(test.get_fileName())

