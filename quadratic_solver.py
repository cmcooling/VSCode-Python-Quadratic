import math

def quadratic_solver(a, b, c, complex_allowed=False):

    if a==0:
        if b==0:
            raise ValueError("Both 'a' and 'b' were zero, meaning there was no defined value for 'x'")
        else:
            return([c/b])

    discriminant=b**2-4*a*c

    if discriminant<0:
        if complex_allowed:
            [(b-1j*math.sqrt(-discriminant))/(2*a), (b+1j*math.sqrt(-discriminant))/(2*a)]
        else:
            raise ValueError("The discrimnant was negative and complex reuslts were not allowed")
    elif discriminant==0:
        return([b/(2*a)])
    else:
        return([(b-math.sqrt(discriminant))/(2*a), (b+math.sqrt(discriminant))/(2*a)])