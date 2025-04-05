x = float(input("Enter x: "))
y = float(input("Enter y: "))

if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-axis")
else:
    print("X-axis")
