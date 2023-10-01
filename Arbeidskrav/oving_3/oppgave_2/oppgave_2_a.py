def find(query, module):

    #result = sorted([f'{get(module.__name__)}.{name}' for name in dir(module) if not name.startswith('_') and query.lower() in name.lower() ], key=len)
    result = sorted([f'{name}' for name in dir(module) if not name.startswith('_') and query.lower() in name.lower() ], key=len)

    for entry in result[:10]:
        print(entry)
    
    return

import sympy as sp

rho = 2         # rho rises
phi = sp.pi/3   # phi falls
theta = sp.pi/4 # theta twirls


punkt = sp.Matrix((rho, phi, theta))

def kule_til_kartesisk(vektor: sp.Matrix):
    rho, phi, theta = vektor

    z = sp.cos(phi)*rho
    x = sp.sin(phi)*sp.cos(theta)*rho
    y = sp.sin(phi)*sp.sin(theta)*rho

    return sp.Matrix((x, y, z))

punkt_kartesisk = kule_til_kartesisk(punkt)

import matplotlib.pyplot as plt

fig_a = plt.figure()
ax = plt.subplot(projection='3d')

ax.quiver(0, 0, 0, *punkt_kartesisk, )

lim = int(punkt_kartesisk.norm())

ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)

#plt.show()

# Oppgave b
import sympy as sp

radius_b = 6        # radius
theta_b = sp.pi/4   # theta twirlz  
z_b = 5             # 

punkt_b = sp.Matrix((radius_b, theta_b, z_b))

def sylinder_til_kartesisk(vektor):
    r, theta, z = vektor

    x = sp.cos(theta)*r
    y = sp.sin(theta)*r

    return sp.Matrix((x, y, z))

punkt_b_kartesisk = sylinder_til_kartesisk(punkt_b)
punkt_b_kartesisk

fig_b = plt.figure()

ax_b = plt.subplot(projection='3d')

ax_b.quiver(0, 0, 0, *punkt_b)

lim = int(punkt_kartesisk.norm())

ax_b.set_xlim(-lim, lim)
ax_b.set_ylim(-lim, lim)
ax_b.set_zlim(-lim, lim)

plt.show()