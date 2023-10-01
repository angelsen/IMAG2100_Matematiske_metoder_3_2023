# Jupyter Notebook: Analysis of Curves in Space

## Required Libraries
import numpy as np
import matplotlib.pyplot as plt

## Functions for the Vectors
def position(t):
    # As we don't have an actual function for r(t), this is a placeholder
    return np.array([t, t**2, t**3])

def velocity(t):
    # Given from the problem
    return np.array([-3, 1, 0])

def acceleration(t):
    # Given from the problem
    return np.array([0, 1, -2])

def unit_tangent(t):
    v = velocity(t)
    mag = np.linalg.norm(v)
    return v / mag

def binormal(t):
    v = velocity(t)
    a = acceleration(t)
    
    v_cross_a = np.cross(v, a)
    mag = np.linalg.norm(v_cross_a)

    return v_cross_a/mag

def unit_normal(t):
    b = binormal(t)
    unit_t = unit_tangent(t)

    return np.cross(b, unit_t)

def binormal_unitTangent_cross_unitNormal(t):
    unit_t = unit_tangent(t)
    unit_n = unit_normal(t)

    return np.cross(unit_t, unit_n)

## Plotting
t_values = np.linspace(0, 2, 250) # Adjust as needed
r_values = np.array([position(t) for t in t_values])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

#ax.plot(r_values[:, 0], r_values[:, 1], r_values[:, 2], label='Curve r(t)')
ax.quiver(position(1)[0], position(1)[1], position(1)[2], *velocity(1), color='r', label='Velocity')
ax.quiver(position(1)[0], position(1)[1], position(1)[2], *acceleration(1), color='b', label='Acceleration')
ax.quiver(position(1)[0], position(1)[1], position(1)[2], *unit_tangent(1), color='g', label='Unit Tangent')
ax.quiver(position(1)[0], position(1)[1], position(1)[2], *unit_normal(1), color='y', label='Unit Normal')
ax.quiver(position(1)[0], position(1)[1], position(1)[2], *binormal(1), color='c', label='Binormal')
ax.quiver(position(1)[0], position(1)[1], position(1)[2], *binormal_unitTangent_cross_unitNormal(1), color='r', label='Binormal `T x N`')

## Setting equal limits
max_limit = 4
min_limit = -max_limit
ax.set_xlim([min_limit, max_limit])
ax.set_ylim([min_limit, max_limit])
ax.set_zlim([min_limit, max_limit])

ax.legend()
plt.show()

#print(sp.Array(binormal(1)))