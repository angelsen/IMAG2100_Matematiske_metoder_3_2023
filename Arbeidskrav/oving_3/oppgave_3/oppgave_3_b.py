import sympy as sp

# Define x, y, and z symbolically
x = expr = sp.Pow(3, sp.Rational(3, 2))
y = 3
z = -3


punkt_kartesisk = sp.Matrix((x, y, z))

def kartesisk_til_kjegle(vektor):
    x,y,z = vektor

    theta = sp.atan2(y, x)
    
    radius = sp.sqrt(sp.Pow(x, 2) + sp.Pow(y, 2))

    return sp.Matrix((radius, theta, z))

punkt_kjegle = kartesisk_til_kjegle(punkt_kartesisk)
print(punkt_kjegle)