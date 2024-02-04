'''
SciPy is a python library used to solve scientific  and mathematical  problems
built on NUMpy
allows manipulation and visualizing of data

#difference between Numpy and Scipy
-both are used for mathematical and numerical analysis
-Numpy contains array data and basic operations
-Scipy consissts of all the numeric code
-SciPy contains fuully-featured versions of mathematical and scientific  functions

# subpackages for  Scipy include cluster, constants ,fftpack,interpolate, etc
-use help(), info(), source().. to know the basic functions'''
from scipy import cluster
help(cluster)


import  scipy
scipy.source(cluster)

# specialfunctiions used in mathMATICS
#EXPONENTIAL
from  scipy import special
a = special.exp10(2)
print(a)
b = special.exp2(3)
print(b)

#Trigonometric
c = special.cosdg(90)
print(c)

c = special.sindg(90)
print(c)

c = special.tandg(90)
print(c)
#intergration function-


#general integration-the quad function calculates the integral of a function which has one variable
#Double integration  -  the dblqud function calculates the  double integral of the fuction with two variables

from scipy import integrate
#print(help(integrate.quad))

i = scipy.integrate.quad(lambda x:special.exp10(x),0,1)
print(i)

#DBLQUAD
e = lambda  x,y:x*y**2
f = lambda x: 1
g = lambda x: -1
integrate.dblquad(e,0,2,f,g)


'''#fourier transformation

fourier analysis is a method that deals with expressing a function as a sum of periodic
components  and recovering the signalfrom the components
the fft and ifft functions can be used to return the discrete fourier transform of a
 real or complex sequence
'''
from scipy.fftpack import ifft,fft
import numpy  as np
x = np.array([1,2,3,4])
y =ifft(x)
print(y)

#linear algebra
from scipy import linalg
a = np.array([[1,2],[3,4]])
b = linalg.inv(a)
print(a)
print(b)
#INTERPOLATION FUNCTIONS
'''
INTERPOLATION refers to constructing new data points within a set of known data points.
the sci.py interpolate consists of spline functions and classes, one-dimensional and multi-dimensional (univariate and multivariate) interpolation classes,etc
 
'''
import matplotlib.pyplot as plt
from scipy import interpolate
x = np.arange(5,20)
y = np.exp(x/3.0)
print(y)
f = interpolate.interp1d(x,y)
x1 = np.arange(6,12)
y1 = f(x1)#use interpolation function returned by 'interpid'
plt.plot(x,y,'o',x1,y1,'--')
plt.show()
