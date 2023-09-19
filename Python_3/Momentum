# 1. Function to calculate linear momentum (p = mv)
def linear_momentum(mass, velocity):
    # Calculate linear momentum (p) given mass and velocity.
    return mass * velocity

# 2. Function to calculate final velocities in an elastic collision
def elastic_collision(mass1, velocity1, mass2, velocity2):
    # Check for division by zero
    if mass1 + mass2 == 0:
        return -1,-1
    # Calculate the final velocities of two objects after an elastic collision.
    v1_final = ((mass1 - mass2) / (mass1 + mass2)) * velocity1 + ((2 * mass2) / (mass1 + mass2)) * velocity2
    v2_final = ((2 * mass1) / (mass1 + mass2)) * velocity1 - ((mass1 - mass2) / (mass1 + mass2)) * velocity2

    return v1_final, v2_final

# 3. Function to calculate final velocity in an inelastic collision
def inelastic_collision(mass1, velocity1, mass2, velocity2):
    # Check for division by zero
    if (mass1 + mass2) == 0:
        return -1
    total_mass = mass1 + mass2
    # Calculate the final velocity of two objects after an inelastic collision.
    final_velocity = (mass1 * velocity1 + mass2 * velocity2) / total_mass

    return final_velocity

# Consuming the Implementations above:
mass1 = 2.0  # kg
velocity1 = 3.0  # m/s
mass2 = 1.5  # kg
velocity2 = -2.0  # m/s

# Calculating the linear momentum
momentum = linear_momentum(mass1, velocity1)
print(f"Linear Momentum: {momentum} kg*m/s")

# Calculating the final velocities in an elastic collision
final_velocities = elastic_collision(mass1, velocity1, mass2, velocity2)
print(f"Elastic Collision - Final Velocities: v1_final = {final_velocities[0]} m/s, v2_final = {final_velocities[1]} m/s")

# Calculating the final velocity in an inelastic collision
final_velocity = inelastic_collision(mass1, velocity1, mass2, velocity2)
print(f"Inelastic Collision - Final Velocity: {final_velocity} m/s")
