import numpy as np
import matplotlib.pyplot as plt

rho_max = 160
L = 5
dx = 0.01
dt = 0.1
num_points = int(2 * L / dx)
num_time_steps = int(120 / dt)
v_max = 120

rho = np.zeros(num_points)
shock = int((L - 0.25) / dx)

rho[shock : 500] = rho_max
rho[0 : shock] = 80

x = np.linspace(-5, 5, num_points)
fig, axs = plt.subplots(2, 2)
m = 0
n = 0

# Lax-Friedrichs Update
for t in range(num_time_steps):
    rho_next = np.copy(rho)

    for i in range(1, num_points):
        i_plus_1 = (i + 1) % num_points
        i_minus_1 = (i - 1) % num_points

        f_iplus1 = v_max * rho[i_plus_1] * (1 - (rho[i_plus_1] / rho_max))
        f_iminus1 = v_max * rho[i_minus_1] * (1 - (rho[i_minus_1] / rho_max))


        updated = ((rho[i_plus_1] + rho[i_minus_1]) / 2) - (dt / dx) * ((f_iplus1 - f_iminus1) / 2)
        
        updated = np.minimum(updated, rho_max)
        rho_next = np.maximum(rho_next, 0)
        rho_next[i] = updated
    
    rho = rho_next
    rho = np.maximum(rho, 0)


    if t in [0, 150, 300, 1199]:
        axs[m, n].plot(x, rho)
        axs[m, n].set_xlabel("x (km)")
        axs[m, n].set_ylabel("Density (cars per m)")
        axs[m, n].set_title(f"Time {t}")
        n += 1
        if n == 2:
            m += 1
            n = 0

plt.subplots_adjust(hspace=0.6)
plt.subplots_adjust(wspace=0.6)

plt.show()
