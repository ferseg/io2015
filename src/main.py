__author__ = 'fsegovia'

# Testing

import fileReader

fr = fileReader.FileReader('/Users/fsegovia/Desktop/ex.py', 'r')

lines = fr.readLines()


for line in lines:
    print(line)

fr.closeFile()


