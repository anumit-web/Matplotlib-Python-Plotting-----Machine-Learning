#   python3 pandas_Read_CSV.py
"""
python3 matplotlib_Matplotlib_Markers.py
"""

import matplotlib
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
 


print("Matplotlib")
print("************************************")


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()


print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()


print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()


print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()


print("---------------------------------------------------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()


print("---------------------------------------------------")


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

