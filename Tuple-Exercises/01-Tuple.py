# Define the tuple
coordinates = (3,4)

# Extract values (x1, y1 = 3,4) and (x2, y2 = 0,0)
x1 = coordinates[0]
y1 = coordinates[1]
x2 = 0
y2 = 0

# Calculate distance
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Print the result
print("-" *35)
print(f"The distance from origin is: {distance}")
print("-" *35)

# Conditional Check
if distance > 4:
    print("The point is far from the origin.")
else:
    print("The point is close to the origin.")
print("-" *35)
