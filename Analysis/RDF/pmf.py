#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE: 

# PREAMBLE:

import numpy as np
import sys

data_file = sys.argv[1]

R = 0.0019872	# units: kcal mol^-1 K^-1
Temp = 230.0
RT = R*Temp

# SUBROUTINES

# MAIN PROGRAM:

data = np.loadtxt(data_file)

nf = open('pmf.dat', 'w')

pmf = 0.0

for i in range(len(data)):
	pmf = -RT*np.log(data[i][2])
	nf.write('%15.6f    %15.6f \n' %(data[i][0], pmf))

nf.close()


