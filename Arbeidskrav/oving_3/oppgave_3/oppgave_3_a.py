import sympy as sp

# x = 15/4
# y = 5*sp.sqrt(3)/4
# z = 5/2

# Define x, y, and z symbolically
x = sp.Rational(15, 4)
y = 5*sp.sqrt(3)/4
z = sp.Rational(5, 2)


punkt_kartesisk = sp.Matrix((x, y, z))

def kartesisk_til_kule(vektor):
    x,y,z = vektor

    theta = sp.atan2(y, x)
    
    h = sp.sqrt(x**2+y**2)
    rho = sp.sqrt(z**2+h**2)

    phi = sp.atan2(h, z)

    return sp.Matrix((rho, phi, theta))

punkt_kule = kartesisk_til_kule(punkt_kartesisk)
print(punkt_kule)

import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.subplot(projection='3d')

ax.quiver(0,0,0, *punkt_kule, color='red', label='punkt_kule' )
ax.scatter(0,0,0)

lim = int(sp.N(punkt_kule.norm()))

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

ax.legend()

plt.show()
