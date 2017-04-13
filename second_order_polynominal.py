"""
This module help to computes the real or imaginary
roots of a second order polynomial.

# Solve the quadratic equation
y = ax^2+bx+c [where a,b and c are real numbers and a != 0]

#using list as the input argument for the function
"""

# import complex math module
import cmath

def cal_roots(argument):
    """
    This function help to computes the real or imaginary
    roots of a second order polynomial.
    """
    #check whether the argument is list or not and length of list must be there.
    try:
        
        if isinstance(argument, list)and len(argument)==3:
            a = argument[0]
            b = argument[1]
            c = argument[2]

            # calculate the discriminant
            d = (b**2) - (4.0*a*c)

            #find the solutions
            sol1 = (-b - cmath.sqrt(d))/(2*a) #first solution
            sol2 = (-b + cmath.sqrt(d))/(2*a) #second solution
            print('The solution are of the quadratic equation {0} and {1}'.format(sol1,sol2)) #print the result
            return(sol1,sol2) #return the result in tuple
        else:
            raise ValueError()
        
    except (ValueError):
        print("Oops!  That was not list argument or length of list is too short.  Please Enter list argument as [a,b,c]!")
        

if __name__=="__main__":
    a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")
    cal_roots([a,b,c])
    
        
        
        
