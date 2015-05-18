#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

data_file = sys.argv[1]

# SUBROUTINES

# MAIN PROGRAM:

data = np.loadtxt(data_file)

plt.plot(data[:,0], data[:,1], label='RDF')

plt.title('Potential of Mean Force for Liquid Argon')
plt.xlabel(r'Distance ($\AA$)')
plt.ylabel(r'PMF ($kcal\ mol^{-1}$)')
plt.ylim((-0.4, 3.0))

plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')

plt.savefig('RDF.png')

