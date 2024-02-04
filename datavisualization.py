#MATPLOTLIB
'''
human brain can process information in pictorial oor graphical form

DV- allows us to quiclkly interpret  the data and adjust different variables to see their effect
DV- it is the presentation of data in pictorial and graphical  format
 thisloop below showcases the whole process
                        -document insight
                         -transform the data set
                         -visualize
                         -analyse
matplotlib is a python package used for 2d graphics

#TGYPES OF PLOTS
-bargraph, Histograms, scatter plot,pie plot, hexagonal bin plot, area plot

from matplotlib import pyplot as plt

plt.plot([1,2,3],[4,5,1])
plt.show()

#labels,
from matplotlib import  pyplot as plt
x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('information')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()

from matplotlib import pyplot as plt
from matplotlib import  style
x=[5,8,10]
y = [12,16,6]

x1 = [6,9,11]
y1 = [6,15,7]

plt.plot(x,y ,"g",label ='line one',linewidth = 5)
plt.plot(x1,y1,'c',label = 'line two',linewidth =5)

plt.title('epic information')
plt.ylabel('y axis')
plt.xlabel('x axis')

plt.legend()
plt.grid(True,color = 'k')
plt.show()

#bar graph used to   compare things betweeen different groups , suited well with changes over tIme

from matplotlib import pyplot as plt
plt.bar([1,3,5,7,9],[5,2,7,8,2],label = 'example one')

plt.bar([2,4,6,8,10],[8,6,2,5,6],label ='example two',color = 'g')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')


plt.title('canvas canvas')
plt.show()
#histogram
from matplotlib import  pyplot as plt
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins =[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages,bins,histtype='bar' ,rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("HIstogram")
plt.legend()
plt.show()'''
#scatter plot
from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
plt.scatter(x,y,label='skitcat',color ='k',s =25,marker = 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter plot')
plt.legend()
plt.show()


#stackplot/areaplot
import matplotlib.pyplot as plt

days=[1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing =[8,7,8,13,9]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('stck plot')
plt.legend()
plt.show()

#piecharts

import matplotlib.pyplot as plt
slices =[7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors = cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%'
        )

plt.title('piechart')
plt.show()

#working with multiple plots
import numpy as np
import matplotlib.pyplot as plt

def f(t):
        return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,0.5,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.subplot(221)
plt.plot(t1,f(t1),'bo',t2, f(t2))

plt.subplot(222)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()
