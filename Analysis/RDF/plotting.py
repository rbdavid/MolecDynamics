#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

data_file = sys.argv[1]

# SUBROUTINES

# MAIN PROGRAM:

data = np.loadtxt(data_file)

plt.plot(data[:,0], data[:,2], label='RDF')

plt.title('Radial Distribution Function')
plt.xlabel(r'Distance ($\AA$)')
plt.ylabel(r'G(r)')
plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')

plt.savefig('RDF.png')

