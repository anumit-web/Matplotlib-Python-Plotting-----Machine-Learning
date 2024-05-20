#   python3 pandas_Read_CSV.py
"""
python3 matplotlib_Matplotlib_Line.py
"""

import matplotlib
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
 


print("Matplotlib")
print("************************************")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()


print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = ':')
plt.show()


print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = '#4CAF50')
plt.show()


print("---------------------------------------------------")


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

print("---------------------------------------------------")

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

print("---------------------------------------------------")

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")






"""
x = ["apple", "banana", "cherry"] 	list 	
x = ("apple", "banana", "cherry") 	tuple
x = {"name" : "John", "age" : 36} 	dict 	
x = {"apple", "banana", "cherry"} 	set
"""

"""
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple
x = dict(name="John", age=36) 	            dict 	
x = set(("apple", "banana", "cherry")) 	    set
"""

