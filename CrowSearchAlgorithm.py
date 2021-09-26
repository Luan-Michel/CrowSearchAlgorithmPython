# -------------------------------------------------
# Citation details:
# Alireza Askarzadeh, Anovel metaheuristic method for solving constrained
# engineering optimization problems: Crow search algorithm, Computers &
# Structures, Vol. 169, 1-12, 2016.
# Programmed by Alireza Askarzadeh at Kerman Graduate #
# University of Advanced Technology(KGUT) #
# Date of programming: September 2015 #
# -------------------------------------------------
# This demo only implements a standard version of CSA for minimization of
# a standard test function(Sphere) on MATLAB 7.6.0 (R2008a).
# -------------------------------------------------
# Note:
# Due to the stochastic nature of meta-heuristc algorithms, different runs
# may lead to slightly different results.
# -------------------------------------------------
# Simple transcripted to SciLab by Luan Michel(github.com/Luan-Michel/CrowSearchAlgorithmPython)
# Original in https: # www.mathworks.com/matlabcentral/fileexchange/56127-crow-search-algorithm

import random	#random Function
import numpy 	#numpy operations
import math		#ceil function

def init(n, pd, l, u): #init the matrix problem
	x = []
	for i in range (n):
		x.append([])
		for j in range (pd):
			x[i].append(l-(l-u)*(random.random()))
	return x

def fitness(xn, n ,pd):	#function for fitness calculation
    fitness = []
    for i in range(n):
        fitness.append(0)
        for j in range(pd):
            fitness[i] = fitness[i]+pow(xn[(i, j)], 2)
    return fitness

# variables initialization #
pd = 10		#Problem dimension (number of decision variables)
n = 20		#Flock (population) size
ap = 0.1	#Awareness probability
fl = 2		#Flight length (fl)
l = -100	#Lower
u = 100		#Uper
x = numpy.matrix(init(n, pd, l, u))
xn = x.copy()
ft = numpy.array(fitness(xn, n, pd))
mem = x.copy()			#Memory initialization
fit_mem = ft.copy()		#Fitness of memory positions
tmax = 1000				#Max numuber of iterations (itermax)
ffit = numpy.array([])	# Best fit of each iteration

#Iteration begin

for t in range(tmax):

	num = numpy.array([random.randint(0, n-1) for _ in range(n)]) # Generation of random candidate crows for following (chasing)
	xnew = numpy.empty((n,pd))
	for i in range (n):
		if(random.random() > ap):
			for j in range (pd):
				xnew[(i,j)] = x[(i,j)]+fl*((random.random())*(mem[(num[i],j)]-x[(i,j)]))
		else:
			for j in range (pd):
				xnew[(i, j)] = l-(l-u)*random.random()
	xn = xnew.copy()
	ft = numpy.array(fitness(xn, n, pd)) #Function for fitness evaluation of new solutions

	#Update position and memory#
	for i in range(n):
		if(xnew[i].all() > l and xnew[i].all() < u):
			x[i] = xnew[i].copy()		#Update position
			if(ft[i] < fit_mem[i]):
				mem[i] = xnew[i].copy()	#Update memory
				fit_mem[i] = ft[i]
	ffit = numpy.append(ffit, numpy.amin(fit_mem)) 	#Best found value until iteration t

ngbest, = numpy.where(numpy.isclose(fit_mem, min(fit_mem)))
print(mem[ngbest[0]])
