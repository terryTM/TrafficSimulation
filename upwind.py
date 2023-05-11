import numpy as np
import matplotlib.pyplot as plt

rho_max = 160
L = 5
dx = 0.01
dt = 0.1  # Convert dt from seconds to hours
num_points = int(2 * L / dx)
num_time_steps = int(120 / dt)
v_max = 120

rho = np.zeros(num_points)
shock = int((L - 0.25) / dx)

rho[shock : 500] = rho_max
rho[0 : shock] = 80

#print(rho)

x = np.linspace(-5, 5, num_points)
fig, axs = plt.subplots(2, 2)
m = 0
n = 0

# Upwind
rho_next = np.copy(rho)
for t in range(num_time_steps):
    #print(t)
    for i in range(0, num_points - 1):
        updated = rho[i] - (dt / dx) * v_max * (rho[i + 1] * (1 - rho[i + 1] / rho_max) - rho[i] * (1 - rho[i] / rho_max))
        updated = np.maximum(updated, 0)
        updated = np.minimum(updated, rho_max)
    
        rho_next[i] = updated
    
    updated = rho[-1] - (dt / dx) * v_max * (rho[0] * (1 - rho[0] / rho_max) - rho[-1] * (1 - rho[-1] / rho_max))
    updated = np.maximum(updated, 0)
    updated = np.minimum(updated, rho_max)
    rho_next[-1] = updated

    
    rho = rho_next

    if t in [0, 150, 300, 1199]:
        if t == 0:
            axs[m, n].plot(x, rho)
            axs[m, n].set_xlabel("x (km)")
            axs[m, n].set_ylabel("Density (cars per km)")
            axs[m, n].set_title("Time 0")
        elif t == 150:
            axs[m, n].plot(x, rho)
            axs[m, n].set_xlabel("x (km)")
            axs[m, n].set_ylabel("Density (cars per km)")
            axs[m, n].set_title("Time 150")
        elif t == 300:
            axs[m, n].plot(x, rho)
            axs[m, n].set_xlabel("x (km)")
            axs[m, n].set_ylabel("Density (cars per km)")
            axs[m, n].set_title("Time 300")
        elif t == 1199:
            axs[m, n].plot(x, rho)
            axs[m, n].set_xlabel("x (km)")
            axs[m, n].set_ylabel("Density (cars per km)")
            axs[m, n].set_title("Time 1200")
        n += 1
        if n == 2:
            m += 1
            n = 0


plt.subplots_adjust(hspace=0.6)
plt.subplots_adjust(wspace=0.6)

plt.show()



print(rho)

# Plotting the results
#x = np.linspace(-5, 5, num_points)
#plt.plot(x, rho)
#plt.xlabel("x (km)")
#plt.ylabel("Density (cars per km)")
#plt.show()
