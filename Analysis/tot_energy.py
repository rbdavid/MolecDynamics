#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:

# PREAMBLE:

import numpy as np
import matplotlib.pyplot as plt
import sys

time_file = sys.argv[1]
totEN_file = sys.argv[2]
potEN_file = sys.argv[3]
kinEN_file = sys.argv[4]

# SUBROUTINES

# MAIN PROGRAM:

time = np.loadtxt(time_file)
totEN = np.loadtxt(totEN_file)
potEN = np.loadtxt(potEN_file)
kinEN = np.loadtxt(kinEN_file)

plt.plot(time[:100], totEN[:100], 'r', label = 'Total Energy')
plt.plot(time[:100], potEN[:100], 'b', label = 'Potential Energy')
plt.plot(time[:100], kinEN[:100], 'g', label = 'Kinetic Energy')

plt.title('Energies of the Liquid Ar system - 1st 100 steps')
plt.legend(bbox_to_anchor = (0.91, 0.65), bbox_transform=plt.gcf().transFigure)
plt.xlabel(r'Time $(ps)$')
plt.ylabel(r'Energy $(kcal\ mol^{-1})$')
plt.grid(b=True, which='major', axis='both', color='#808080', linestyle='--')

plt.savefig('ENvsTIME.100steps.png')

