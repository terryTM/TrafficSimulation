import numpy as np
import matplotlib.pyplot as plt

# Constants
num_cars = 30  # 10% occupancy
v_max = 5
road_length = 2250  # 2.25 km
num_steps = 100  # 100 seconds
num_cells = 300

# Initialize positions and velocities randomly
positions = np.random.choice(np.arange(num_cells), size=num_cars, replace=False)
positions.sort()


velocities = np.random.randint(0, v_max + 1, size=num_cars)

def update_positions(positions, velocities):
    updated_positions = positions.copy()
    updated_velocities = velocities.copy()
    
    for i in range(num_cars):
        distance_to_next = positions[(i + 1) % num_cars] - positions[i] - 1
        if distance_to_next < 0:
            distance_to_next += num_cells

        # Rule 1: Accelerate v_i := min{v_i + 1, v_max}
        updated_velocities[i] = min(velocities[i] + 1, v_max)

        # Rule 2: Decelerate v_i := d(i, i+1), if v_i > d(i, i + 1)
        if updated_velocities[i] > distance_to_next:
            updated_velocities[i] = distance_to_next

        # Rule 3: Move vehicle i moves v_i cells forward
        updated_positions[i] = (positions[i] + updated_velocities[i]) % num_cells

    return updated_positions, updated_velocities

# Run the simulation
positions_history = [positions]
velocities_history = [velocities]

for i in range(num_steps):
    positions, velocities = update_positions(positions, velocities)
    positions_history.append(positions)
    velocities_history.append(velocities)

# Plot the results
density = np.zeros((num_steps + 1, num_cells))
for step, (positions, velocities) in enumerate(zip(positions_history, velocities_history)):
    density[step, positions] = velocities 


plt.imshow(density, aspect='auto', origin='upper', cmap='Greys')
plt.xlabel("Position (m)")
plt.ylabel("Time (s)")

plt.gca().xaxis.tick_top()
plt.gca().xaxis.set_label_position('top')

plt.title("Simulation of Road")
plt.show()