from fileReader import *

COMPARISON_OPERATORS = [">","<"]
EQ_OPERATOR = "="

CONTENT_ERROR = "El archivo posee caracteres inválidos"

class readerLP(FileReader):
    'Reads Linear Programming files'
    def __init__(self, fileName, options):
        self.file = open(fileName, options)
        self.clear_data()

    def get_validity(self):
        return self.validity
    def get_maxmin(self):
        return self.__maxmin
    def get_FO(self):
        return self.__objective
    def get_inequations(self):
        return self.__inequations

    def clear_data(self):
        self.validity=True
        self.__objective=[]
        self.__inequations=[]
        self.__maxmin=0
        self.__error=""
        
    def get_LP(self):
        self.clear_data()
        try:
            lines=self.readLines()
            #defines if we need to maximize or minimize the function
            self.get_LP_maxmin(lines[0])
            lines=lines[1:]

            #gets the objective function
            self.get_LP_Function(lines[:2])
            lines=lines[2:]

            #gets the inequations
            self.get_LP_Inequations(lines)
        except:
            #invalid file
            self.set_warning()
            #invalid file

    def get_LP_maxmin(self,string):
        self.check_int(string)
        number = int(string)
        if number > 1 or number < 0:
            self.set_warning()
        self.__maxmin = number

    def get_LP_Function(self,lines):
        if len(lines)==2:
            for i in lines:
                self.check_int(i)
                self.__objective += [float(i)]
        else:
            self.set_warning()

    def get_LP_Inequations(self,lines):
        cont=0
        temp=lines[:5]
        while len(lines)>0:
            temp=lines[:5]
            self.list_to_inequation(temp,2)
            lines=lines[5:]
        return

    def list_to_inequation(self,lines,variables):
        cont = 0
        temp = []
        temp2 = ""
        if len(lines) == 5:
            while cont<variables:
                self.check_int(lines[cont])
                temp += [float(lines[cont])]
                cont += 1
            lines = lines[variables:]
            if lines[0] in COMPARISON_OPERATORS:
                if lines[1] == EQ_OPERATOR:
                    temp2 += lines[0] + lines[1]
                    self.check_int(lines[2])
                    temp += [temp2] + [float(lines[2])]                
                    cont = 0
                    while cont<variables:
                        if temp[cont]!=0:
                            self.__inequations += [temp]
                            return
                        cont += 1
                    return
        self.set_warning()

    def check_int(self,string):
        """
        checks that the string can be converted to a float
        """
        try:
            float(string)
        except:
            self.set_warning()

    def set_warning(self):
        self.validity = False
        self.__error = CONTENT_ERROR

    def to_string(self):
        if self.validity:
            print("Validez: " + str(self.validity))
            print("Max o Min: " + str(self.__maxmin))
            print("FO: " + str(self.__objective))
            print("Inequations: " + str(self.__inequations))
        else:
            print(self.__error)

#example
a = readerLP("test.txt","r")
a.get_LP()
a.to_string()

#getting data
#a.get_validity()
#a.get_maxmin()
#a.get_FO()
#a.get_inequations()