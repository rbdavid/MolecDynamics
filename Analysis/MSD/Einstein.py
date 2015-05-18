#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:

# PREAMBLE:

import numpy as np
import sys
import MDAnalysis

psf = sys.argv[1]
traj = sys.argv[2]

# SUBROUTINES:

# MAIN PROGRAM:

buf = 100

deltaWrite = 10.0
delta_t = 0.002
box_dim = 28.40         # xyz file does not hold this info (even though it does); for NPT, the dcd file will contain this info; must comment out this line

nf = open('einstein.dat', 'w')

# set the universe object
u = MDAnalysis.Universe('%s' %(psf), '%s' %(traj))

nAtoms = len(u.atoms)
nSteps = len(u.trajectory)		# this line selects all steps to analyze (WAAAAY TOO MANY)...
maxDeltaStep = nSteps - 1 - buf

print nAtoms, nSteps

coor = np.zeros((nSteps,nAtoms, 3))

dist2AutoCorr = np.zeros((maxDeltaStep))

for ts in u.trajectory[1:]:
	i = u.trajectory.frame -2
	if i%100==0:
		print('Reading step %d from trajectory file \n' %(i))

	for atom in range(0,nAtoms):
		coor[i][atom] = u.atoms[atom].position

for deltaStep in range(1,maxDeltaStep):
	count = 0
	sumdist2 = 0.0

	if deltaStep%10==0:
		print('Working on correlation for deltaStep = %10d\n' %(deltaStep))
	
	for step1 in range(0,nSteps-deltaStep):
		step2 = step1+deltaStep
		
		for atom in range(0,nAtoms):
			dist2 = 0.0
		
			for i in range(0,3):
				dist = coor[step1][atom][i] - coor[step2][atom][i]
				if dist <-box_dim/2.0:
					dist += box_dim
				if dist >box_dim/2.0:
					dist -= box_dim
				dist2 += dist**2
			
			sumdist2 += dist2
			count += 1.0
	
	dist2AutoCorr[deltaStep] = sumdist2/float(count)
	nf.write('%10.6f    %30.15f \n' %(deltaStep*deltaWrite*0.002, dist2AutoCorr[deltaStep]))

nf.close()

