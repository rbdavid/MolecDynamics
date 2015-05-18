#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

# USAGE:  ./GreenKubo.py ../../liq_ar.pdb ../../Data/liq_ar.veldcd > diffusion_coeff.dat 

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

nf = open('greenkubo.dat', 'w')

# set the universe object
u = MDAnalysis.Universe('%s' %(psf), '%s' %(traj), format='DCD')

nAtoms = len(u.atoms)
nSteps = len(u.trajectory)		# this line selects all steps to analyze (WAAAAY TOO MANY)...
maxDeltaStep = nSteps - 1 - buf

print nAtoms, nSteps

vel = np.zeros((nSteps,nAtoms, 3))

vel2AutoCorr = np.zeros(maxDeltaStep)

for ts in u.trajectory[1:]:
	i = u.trajectory.frame -2
	if i%100==0:
		print('Reading step %d from trajectory file \n' %(i))

	for atom in range(0,nAtoms):
		vel[i][atom] = u.atoms[atom].position

for deltaStep in range(1,maxDeltaStep):
	count = 0
	stepvel2 = 0.0

	if deltaStep%10==0:
		print('Working on correlation for deltaStep = %10d\n' %(deltaStep))
	
	for step1 in range(0,nSteps-deltaStep):
		step2 = step1+deltaStep
		
		for atom in range(0,nAtoms):
			vel2 = 0.0
		
			for i in range(0,3):
				vel2 = vel[step1][atom][i]*vel[step2][atom][i]
			
			stepvel2 += vel2
			count += 1.0
	
	vel2AutoCorr[deltaStep] = stepvel2/float(count)

runningInt = 0.0

for deltaStep in range(0,maxDeltaStep):
	runningInt += vel2AutoCorr[deltaStep]*deltaStep*deltaWrite*delta_t
	nf.write('%10.6f    %30.15f     %30.15f\n' %(deltaStep*deltaWrite*delta_t, vel2AutoCorr[deltaStep], runningInt))

print runningInt

nf.close()

