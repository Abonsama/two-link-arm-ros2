import math
# this code needs four inputs values of xyz and mass m to calculate its inertia values 
x= 0.1
y= 0.1
z=0.1
m=0.1

ixx = 1/12*m*((math.pow(z,2))+(math.pow(y,2)))
iyy = 1/12*m*((math.pow(z,2))+(math.pow(x,2)))
izz = 1/12*m*((math.pow(y,2))+(math.pow(x,2)))
print(ixx)
print(iyy)
print(izz)