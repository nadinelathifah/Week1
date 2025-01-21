# Part 3: question 1)
from math import pi, tan, cos

# We input the values into variables
barrel_height = 1
distance = 0.5
theta = 80*(pi/180)
gravity = 9.81
velocity = 44

projectile = barrel_height + distance*tan(theta) - (gravity*(distance**2))/(2*((velocity*cos(theta))**2))
print(projectile)

print(barrel_height + distance*tan(theta) - (gravity*(distance**2))/(2*(velocity*cos(theta))**2))

projectile_values = 1 + 0.5*tan(theta) - (9.81*(0.5**2))/(2*((44*cos(theta))**2))
print(projectile_values)
