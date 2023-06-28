# Imports
import numpy as np
# Lambda function
f = lambda x : np.log(x)
# Varibles
a = 1
b = 2.718281828**3
n = 4
# Derivative
dx = (b-a)/n
x_left = np.linspace(a,b-dx,n)
x_midpoint = np.linspace(dx/2,b - dx/2,n)
x_right = np.linspace(dx,b,n)
# The Sums
lef = np.sum(f(x_left)/2*x_left * dx)
mid = np.sum(f(x_midpoint)/2*x_midpoint * dx)
rig =np.sum(f(x_right)/2*x_right * dx)
# Output
print( "Unit 5.1 Example 3 for WTW_134 (*_*)")
print("Left Rieman Sum: ",lef)
print("Middle Rieman Sum: ",mid)
print("right Rieman Sum: ",rig)
print("The distance covered in 15 seconds is approximately: ",(lef+rig)/2)