__author__ = 'fsegovia'

# Testing

#import graphicalMethod as gm
import transport as trns
#from sympy import *


"""
y = gm.GraphicalMethod([0.75,1,0],[[1,3,"<=",15],[5,1,"<=",20],[3,4,"<=",24]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([0.75,1,0],[[0,1,"<=",5],[0,1,">=",10],[1,0,"<=",5]],1)
print(y.get_advice())
y.plot()


y = gm.GraphicalMethod([0.75,1,0],[[0,1,"<=",4]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([0.75,1,0],[[1,0,"<=",4]],1)
print(y.get_advice())
y.plot()


y = gm.GraphicalMethod([6,10,0],
	[[1,0,"<=",1000],
	[0,1,"<=",700],
	[1,1,"<=",800],
	[1,1,">=",200]],0)
print(y.get_advice())
y.plot()


y = gm.GraphicalMethod([1,1,0],
	[[2,-1,">=",0],
	[1,1,"<=",150],
	[1,0,">=",40],
	[0,1,">=",20]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([1500,1000,0],
	[[1,1,"<=",3000],
	[1,0,"<=",2000],
	[0,1,"<=",2000]],1)
print(y.get_advice())
y.plot()


y = gm.GraphicalMethod([4,2,0],
	[[2,1,"<=",4],
	[1,-1,"<=",1]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([1,1,0],
	[[2,-1,">=",0],
	[1/2,-1,"<=",0]],1)
print(y.get_advice())
y.plot()

y = gm.GraphicalMethod([1,1,0],
	[[2,-1,">=",0],
	[1/2,-1,"<=",0]],0)
print(y.get_advice())
y.plot()
"""





a = trns.Transport([[3,7,1],[2,2,6]],[800,1500],[1000,700,600])

