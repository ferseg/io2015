__author__ = 'fsegovia'

class FileReader():
    'Reads files'
    def __init__(self, fileName, options):
        self.validity=True
        self.openFile(fileName, options)

    def openFile(self,fileName,options):
        self.file = open(fileName, options)
    
    def closeFile(self):
        self.file.close()

    def readLines(self):
        lines = self.file.readlines()
        self.closeFile()
        lines = self.clean_lines(lines)
        return lines

    def clean_lines(self,lines):
        """
        removes the "\n" and " " of a list of strings
        """
        j=[]
        for i in lines:
            i = i.replace(" ","")
            i = i.replace("\n","")
            if i!="":
                j+=[self.convert_fractions(i)]
        return j

    def convert_fractions(self,element):
        """
        Tries to remove the fractions read, to make
        easier the parse
        """
        if len(element)>=3 and "/" in element:
            temp = element.split("/")
            if len(temp) == 2:
                num1 = temp[0]
                num2 = temp[1]
                try:
                    num1,num2 = int(num1),int(num2)
                    if num2 != 0:
                        return str(num1/num2)
                except:
                    return element
        return element
    
    @staticmethod
    def helloWorld():
        print("Hello yo")

