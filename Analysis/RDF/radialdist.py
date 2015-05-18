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

nf = open('g_r.dat', 'w')

# set the universe object
u = MDAnalysis.Universe('%s' %(psf), '%s' %(traj), format='DCD')

nAtoms = len(u.atoms)
#nSteps = len(u.trajectory)              
#nSteps = 200
nSteps = 1000

print nAtoms, nSteps

box_dim = np.array([28.40, 28.40, 28.40], dtype=np.float32)

dmin, dmax = 0.0, 10.0

coor = np.zeros((nSteps,nAtoms, 3))

for ts in u.trajectory[1:nSteps+1]:
        i = u.trajectory.frame -2
        if i%10==0:
	        print('Reading step %d from trajectory file \n' %(i))

        for atom in range(0,nAtoms):
	        coor[i][atom] = u.atoms[atom].position

#for i in range(len(coor)):
#	print i, coor[i][0]

dist2_array = []
count = 0.0
component = np.zeros(3)

for ts in range(len(coor)):
	
	if ts%10==0:
		print('Working on distance calc for frame = %10d \n' %(ts))

	for atom1 in range(0,nAtoms-1):
		for atom2 in range(atom1+1,nAtoms):
			count += 1.0
			dist2 = 0.0;
			for j in range(0,3):
				component[j] = coor[ts][atom1][j] - coor[ts][atom2][j]
				if component[j] <-box_dim[j]/2.0:
					component[j] += box_dim[j]
				if component[j] >box_dim[j]/2.0:
					component[j] -= box_dim[j]
				dist2 += np.power(component[j],2)
			if dist2 <= 0.0:
				print "negative distance^2"
			dist2_array.append(dist2)

dist_array = np.zeros(len(dist2_array))
np.sqrt(dist2_array, dist_array)

rdf, edges = np.histogramdd(dist_array, bins = 100, range = [(dmin, dmax)])

radii = 0.5*(edges[0][1:] + edges[0][:-1])
delta_r = edges[0][1] - edges[0][0]
density = nAtoms/np.power(box_dim[0],3)
norm = density*count*delta_r
vol = (4./3.)*np.pi*density*(np.power(edges[0][1:],3) - np.power(edges[0][:-1],3))

print "volume values:", vol
print "density (units Ang^-3)", density
print "total number of distances calculated:", count
print "normalization factor (w/out volume) (units: Ang^-3)", norm

corr_rdf =  np.zeros(len(rdf))

for i in range(len(rdf)):
	corr_rdf[i] = rdf[i]/(norm*vol[i])
	nf.write('%15.6f    %15.6f    %15.6f \n' %(edges[0][i], rdf[i], corr_rdf[i]))

nf.close()

