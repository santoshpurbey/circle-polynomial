"""
This module help to computes the real or imaginary
roots of a second order polynomial.

# Solve the quadratic equation
y = ax^2+bx+c [where a,b and c are real numbers and a != 0]

#using list as the input argument for the function
"""

# import complex math module
import cmath

def roots(argument):
    if isinstance(argument, list)and len(argument)==3:
        a = argument[0]
        b = argument[1]
        c = argument[2]

        # calculate the discriminant
        d = (b**2) - (4.0*a*c)

        #find the solutions
        sol1 = (-b - cmath.sqrt(d))/(2*a)
        sol2 = (-b + cmath.sqrt(d))/(2*a)
        print('The solution are {0} and {1}'.format(sol1,sol2))
        return(sol1,sol2)

if __name__=="__main__":
    a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")
    roots([a,b,c])
    
        
        
        
