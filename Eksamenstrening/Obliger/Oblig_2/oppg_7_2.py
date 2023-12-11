# Re-importing and setting up the plot after the reset
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define theta range and corresponding g(theta) = e^(3*theta) and its derivative g'(theta)
theta_vals = np.linspace(0, 2, 300)
g_theta_vals = np.exp(3 * theta_vals)
g_prime_theta_vals = 3 * np.exp(3 * theta_vals)  # Derivative of e^(3*theta)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting the curve
ax.plot(theta_vals, g_theta_vals, g_prime_theta_vals, label=r'$g(\theta) = e^{3\theta}$ and $g\'(\theta)$', color='blue')

# Plotting the radial and tangential components
num_elements = 10  # Number of elements to display
theta_sample_vals = np.linspace(0, 2, num_elements)
dtheta = 0.1  # A small value for visualization of differential elements

for theta in theta_sample_vals:
    r = np.exp(3 * theta)
    dr_dtheta = 3 * np.exp(3 * theta)

    # Radial component (r dtheta)
    x_radial = r * np.cos(theta + dtheta) - r * np.cos(theta)
    y_radial = r * np.sin(theta + dtheta) - r * np.sin(theta)

    # Tangential component (dr/dtheta dtheta)
    x_tangential = dr_dtheta * dtheta * np.cos(theta)
    y_tangential = dr_dtheta * dtheta * np.sin(theta)

    # Plotting each component as a line segment
    ax.quiver(theta, r, dr_dtheta, x_radial, y_radial, 0, color='green', length=0.1, normalize=True)
    ax.quiver(theta, r, dr_dtheta, x_tangential, y_tangential, dtheta, color='red', length=0.1, normalize=True)

# Labels and title
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$g(\theta)$')
ax.set_zlabel(r"$g'(\theta)$")
ax.set_title('3D Plot with Radial and Tangential Components')

# Show plot
plt.show()