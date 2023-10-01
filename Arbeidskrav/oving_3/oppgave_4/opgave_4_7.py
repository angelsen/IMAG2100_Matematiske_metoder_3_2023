import sympy as sp

radius, theta, z = sp.symbols('radius theta z')

# $\sqrt{r^{2}+z^{2}}=2$ i sylinderkoordinater.
eq_7 = sp.Eq(sp.sqrt(radius**2 + z**2), 2) 

radius_eq = sp.solve(eq_7, radius)

#radius_eq

positiv_løsning_radius_eq = radius_eq[1]

x = positiv_løsning_radius_eq * sp.cos(theta)
y = positiv_løsning_radius_eq * sp.sin(theta)

p_7 = sp.plotting.plot3d_parametric_surface(x, y, z, (theta, 0, 2*sp.pi), title=r'$\sqrt{r^{2}+z^{2}}=2$')
