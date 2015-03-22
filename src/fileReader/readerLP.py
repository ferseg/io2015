from fileReader import *

VARS=["z","x","y"]

COMPARISON_OPERATORS = [">","<"]
MUL_OPERATOR = "*"
SUM_OPERATOR = "+"
EQ_OPERATOR = "="
NO_OPERATOR = ""

ERROR_CONTENIDO = "El archivo posee caracteres inválidos"

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
        self.__objective=""
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
            self.get_LP_Function(lines[:3])
            lines=lines[3:]

            #gets the inequations
            self.get_LP_Inequations(lines)
        except:
            #invalid file
            self.validity = False
            self.__error = ERROR_CONTENIDO
            #invalid file
        #True or False
        return self.validity

    def get_LP_maxmin(self,string):
        self.check_int(string)
        number = int(string)
        if number > 1 or number < 0:
            self.validity = False
            self.__error = ERROR_CONTENIDO
        self.__maxmin = number

    def get_LP_Function(self,lines):
        cont = 0
        temp = ""
        if len(lines)==3:
            for i in lines:
                self.check_int(i)
                if cont == 0:
                    self.__objective =  append_var(NO_OPERATOR,VARS[cont],i) + EQ_OPERATOR
                elif cont == 1 or temp == "":
                    temp +=  append_var(NO_OPERATOR,VARS[cont],i)
                else:
                    temp += append_var(SUM_OPERATOR,VARS[cont],i)
                cont+=1
            self.__objective += temp
            return lines
        else:
            self.validity = False
            self.__error = ERROR_CONTENIDO

    def get_LP_Inequations(self,lines):
        cont=0
        temp=lines[:5]
        while len(lines)>0:
            temp=lines[:5]
            self.list_to_inequation(temp)
            lines=lines[5:]
        return

    def list_to_inequation(self,lines):
        cont = 0
        temp = ""
        if len(lines)==5:
            while cont < 2:
                self.check_int(lines[cont])
                if cont == 0 or temp == "":
                    temp += append_var(NO_OPERATOR,VARS[cont+1],lines[cont])
                else:
                    temp += append_var(SUM_OPERATOR,VARS[cont+1],lines[cont])
                cont+=1
            lines=lines[2:]
            if lines[0] in COMPARISON_OPERATORS == False:
                self.validity = False
                self.__error = ERROR_CONTENIDO
                return
            temp += lines[0]
            lines = lines[1:]
            if lines[0] != "=":
                self.validity = False
                self.__error = ERROR_CONTENIDO
                return
            temp += lines[0]
            lines = lines[1:]
            if lines[0] == []:
                self.validity = False
                self.__error = ERROR_CONTENIDO
                return
            self.check_int(lines[0])
            temp += lines[0]
            self.__inequations.append(temp)
        else:
            self.validity = False
            self.__error = ERROR_CONTENIDO         

    def check_int(self,string):
        """
        checks that the string can be converted to a int
        """
        try:
            float(string)
        except:
            self.validity = False
            self.__error = ERROR_CONTENIDO

    def to_string(self):
        if self.validity:
            print("Validez: " + str(self.validity))
            print("Max o Min: " + str(self.__maxmin))
            print("FO: " + str(self.__objective))
            print("Inequations: " + str(self.__inequations))
        else:
            print(self.__error)

def append_var(operator,var,number):
    """ appends number * variable, for example 4*x """
    temp = ""
    if number == "0":
        temp = ""
    elif number == "1":
        temp = operator+var
    else:
        temp = operator+number+MUL_OPERATOR+var
    temp = temp.replace("+-","-")
    return temp

#example
a=readerLP("C:/Users/Kenneth/Desktop/test2.txt","r")
a.get_LP()
a.to_string()

#getting data
#a.get_validity()
#a.get_maxmin()
#a.get_FO()
#a.get_inequations()
