import numpy as np
from numpy import sqrt as SQRT

def quadfunc(a, b, c):
        x = (-b + SQRT(b**2 -4*a*c))/(2*a)
        y = (-b - SQRT(b**2 -4*a*c))/(2*a)
        return ('your two roots are ', x, ',', y)