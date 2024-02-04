'''
Numpy is the core library for scientific computing in python
It providesa high-performance multidimensional array object, and tools for working with these
arrays
'''

import numpy as np

#a = np.array([(1,2,3,4),(5,6,7,8)])
#print(a)

"""
numpy vs list

-less memory
-fast
-convenient
"""

import time
import sys

s = range(1000)
print(sys.getsizeof(5)*len(s))
d = np.arange(1000)
print(d.size*d.itemsize)




