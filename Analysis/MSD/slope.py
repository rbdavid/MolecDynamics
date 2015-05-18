#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy as np
import sys
import scipy
from scipy import stats

data_file = sys.argv[1]

data = np.loadtxt(data_file)

slope, intercept, r_value, p_value, std_err = stats.linregress(data[499:2499,0], data[499:2499,1])

nf = open('linear_reg.dat', 'w')

nf.write("Linear Regression for data between %5d ps (frame: 499) and %5d ps (frame 2499) \n" %(data[499][0], data[2499][0]))
nf.write("slope: %10.5E Angstrom^2 ps^-1 \n" %(slope))
nf.write("intercept: %10.5E Angstrom^2\n" %(intercept))
nf.write("R^2: %10.5f \n" %(r_value**2))

nf.write('Diffusion coeff: %10.5E Angstrom^2 ps^-1$ \n' %(slope/6.0))
nf.write('Diffusion coeff: %10.5E m^2 s^-1$ \n' %(slope*10**(-8)/6.0))

nf.close()


