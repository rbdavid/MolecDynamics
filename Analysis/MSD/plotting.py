#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys

data_file = sys.argv[1]

# SUBROUTINES

# MAIN PROGRAM:

data = np.loadtxt(data_file)

plt.plot(data[:,0], data[:,1], label='MSD')

plt.title('Mean-squared Displacement versus time')
plt.xlabel('Time (ps)')
plt.ylabel(r'MSD ($\AA^{2}$)')
#plt.figtext(0.15, 0.75, 'deltaWrite = 10;\n delta_t = 0.002 fs;\n NVE, Homebrew MD', bbox=dict(fc='OrangeRed', alpha=0.5), fontsize=14)
#plt.figtext(0.3, 0.15, 'Diffusion Coefficient = 5.49560E-01 $\AA^{2} ps^{-1}$ \nD = 5.49560E-09 $m^2 s^{-1}$', bbox=dict(fc ='LightGreen', alpha=0.5), fontsize=14)
plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')

plt.savefig('MM_MSD.png')

