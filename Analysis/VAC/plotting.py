#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

data_file = sys.argv[1]

# SUBROUTINES

# MAIN PROGRAM:

data = np.loadtxt(data_file)

plt.plot(data[:,0], data[:,1], label='VAC')

plt.title('Velocity Autocorrelation versus time')
plt.xlabel(r'Time ($ps$)')
plt.ylabel(r'VAC ($\AA^{2} ps^{-2}$)')
#plt.figtext(0.25, 0.75, 'deltaWrite = 10;\n delta_t = 0.002 fs;\n NVE, Homebrew MD', bbox=dict(fc='OrangeRed', alpha=0.5), fontsize=14)
#plt.figtext(0.3, 0.3, 'Diffusion Coefficient = 2487.9229 $\AA^{2} ps^{-1}$ \nD = 2.487E-05 $m^2 s^{-1}$', bbox=dict(fc ='LightGreen', alpha=0.5), fontsize=14)
plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')

plt.savefig('MM_VAC.png')

