# Ladder pattern program

# Prompt for height
height = int(input("Enter maximum height: "))

# Top half (increasing stars)
for i in range(1, height + 1):
    print("* " * i)

# Bottom half (decreasing stars)
for i in range(height - 1, 0, -1):
    print("* " * i)
