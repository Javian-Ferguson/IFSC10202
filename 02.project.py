from math import sin, cos, acos, pi

print("Great Circle Calculator")

# Input values
r = float(input("Enter Radius of Sphere: "))

x1 = float(input("Starting Point - Enter Latitude: "))
y1 = float(input("Starting Point - Enter Longitude: "))
x2 = float(input("Ending Point - Enter Latitude: "))
y2 = float(input("Ending Point - Enter Longitude: "))

# Convert degrees to radians
x1 = x1 * pi / 180
y1 = y1 * pi / 180
x2 = x2 * pi / 180
y2 = y2 * pi / 180

# Apply great-circle distance formula
d = r * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

# Print rounded result
print(f"The Great Circle Distance is {d:.2f}")