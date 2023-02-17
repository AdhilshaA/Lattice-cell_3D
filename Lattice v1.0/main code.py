import currlibrary as lib
from math import pi

# lattice parameter
a = 1
b = 1
c = 1
alpha =90
beta =90
gamma =90

#angle to radians
alpha *= pi/180
beta *= pi/180
gamma *= pi/180


## ALTERNATE: lattice vectors ##
a1 = [1,0,0]
a2 = [0,1,0]
a3 = [0,0,1]
latvec = [a1,a2,a3]

# plane indices
h = 0
k = 0
l = 1

# print("cell points by paramters",lib.gen_cellpoints_v1(a,b,c,alpha,beta,gamma))
# print("cell points by vectors",lib.gen_cellpoints_v2(latvec))

# calculating lattice vectors from lattice parameters.
latvec = lib.gen_latvec_v1(a,b,c,alpha,beta,gamma) 
print("latvec: ",latvec)


normal = lib.gen_normal(latvec,[h,k,l])
print("normal vector",normal)
print("normal's angles with axes:",lib.angleswithaxes((normal)))