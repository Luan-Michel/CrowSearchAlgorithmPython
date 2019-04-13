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

def randomArray(n):	#function that return random array
        rd = []
        for i in range(n):
               rd.append(int(math.ceil(n*random.random())-1))
        return rd

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
	num = numpy.array(randomArray(n)) #Generation of random candidate crows for following (chasing)
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
print(ffit)
