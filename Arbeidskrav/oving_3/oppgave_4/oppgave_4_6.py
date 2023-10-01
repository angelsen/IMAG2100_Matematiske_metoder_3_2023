import sympy as sp

#definer variables

rho, phi, theta = sp.symbols('rho phi theta')

x = rho * sp.sin(phi) * sp.cos(theta)
y = rho * sp.sin(phi) * sp.sin(theta)
z = rho * sp.cos(phi)

xyz = sp.Matrix((x, y, z))

rho_eq = 2 * sp.sin(theta)

p_6 = sp.plotting.plot3d_parametric_surface(*xyz.subs(rho, rho_eq), (phi, 0, sp.pi), (theta, 0, 2*sp.pi), 
                                            title=r"Plot of $\rho=2 \sin (\phi)$", xlabel="X", ylabel="Y")