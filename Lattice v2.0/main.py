import currlibrary as lib
from math import pi
from numpy import array,append

globals().update(lib.parse('input.txt'))  #getting those variables into this code
# update this path depending upon where your current directory is.


# # lattice lengths
# a = 1.0
# b = 1.0
# c = 1.0
# latlen = array([a,b,c])

# # lattice lengths
# alpha =90.0
# beta =90.0
# gamma =90.0
# latang = array([alpha,beta,gamma])

# ## ALTERNATE: lattice vectors ##
# a1 = array([1.0,0.0,0.0])
# a2 = array([0.0,1.0,0.0])
# a3 = array([0.0,0.0,1.0])
# latvec = array([a1,a2,a3])

# # plane indices
# h = 0.0
# k = 0.0
# l = 1.0
# planehkl = array([h,k,l])


# calculating lattice vectors from lattice parameters.
# latvec = lib.gen_latvec_v1(*latlen,*latang) 
# # print("latvec: \n",latvec)
print("##----------------INPUTS-----------------##")
print("\nlattice parameters: ",latlen,latang,"\n")
lib.gen_normal(latlen, latang, planehkl, figure = True)
# print("normal vector:\n",normal)
# print("normal's angles with axes:\n",lib.angleswithaxes((normal)))