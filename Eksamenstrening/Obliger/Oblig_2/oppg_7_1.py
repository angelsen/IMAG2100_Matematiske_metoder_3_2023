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

# Plotting
ax.plot(theta_vals, g_theta_vals, g_prime_theta_vals, label=r'$g(\theta) = e^{3\theta}$ and $g\'(\theta)$')

# Labels and title
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$g(\theta)$')
ax.set_zlabel(r"$g'(\theta)$")
ax.set_title('3D Plot of Theta, g(Theta), and g\'(Theta)')

# Show plot
plt.show()
