__author__ = 'fsegovia'

# Testing

import graphicalMethod as gm
import transport as trns



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






a = trns.Transport([[3,7,1],[2,2,6]],[800,1500],[1000,700,600])

a = trns.Transport([[50,60,10],[25,40,20]],[500,400],[200,300,400])

a = trns.Transport([[100,150,200],[150,120,180]],[4000,5000],[2000,3000,4000])

a = trns.Transport([[3,2.5,3.5],[2.25,3.75,4]],[5000,7000],[3500,4000,4500])
