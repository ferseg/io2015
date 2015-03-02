__author__ = 'fsegovia'

import fileReader

fr = fileReader.FileReader('/Users/fsegovia/Desktop/ex.py', 'r')

lines = fr.readLines()

var = "some"


for line in lines:
    if (line != "\n" and not(line.__contains__("\n"))):
        print(line)

fr.closeFile()


