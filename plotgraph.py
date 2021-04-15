import numpy as np
import pylab

# read a text file using loadtext. the whole file is read into an np.array
whole = np.loadtxt("store.txt", delimiter=" ")

x = whole[:,0]   # zero column which is neighbourhood
y = whole[:,1]   # first column which is total stored

z=y/x   # average store per agent

pylab.plot(x,y)
pylab.xlabel("neighbourhood distance")
pylab.ylabel("units stored")
pylab.show()



