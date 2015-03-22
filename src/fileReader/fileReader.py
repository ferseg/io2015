__author__ = 'fsegovia'

class FileReader():
    'Reads files'
    def __init__(self, fileName, options):
        self.openFile(fileName, options)

    def openFile(self,fileName,options):
        self.file = open(fileName, options)
    
    def closeFile(self):
        self.file.close()

    def readLines(self):
        lines = self.file.readlines()
        self.closeFile()
        lines = self.remove_endOfLines(lines)
        return lines

    def remove_endOfLines(self,lines):
        """
        removes the "\n" at the end on the indexes of a list of strings
        """
        j=[]
        for i in lines:
            j+=[i.replace("\n","")]
        return j
    
    @staticmethod
    def helloWorld():
        print("Hello yo")
