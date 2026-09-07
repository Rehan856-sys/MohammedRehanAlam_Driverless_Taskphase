def distance_squared(point, reference):

    x, y = point
    xr, yr = reference

    return (x - xr) ** 2 + (y - yr) ** 2


def sort_by_distance(points, reference):

    n = len(points)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if distance_squared(points[j], reference) < \
               distance_squared(points[min_index], reference):

                min_index = j

        points[i], points[min_index] = \
            points[min_index], points[i]

    return points


# Input number of points
n = int(input("Enter number of points: "))

points = []

# Input each point
for i in range(n):
    x = int(input(f"Enter x-coordinate of point {i + 1}: "))
    y = int(input(f"Enter y-coordinate of point {i + 1}: "))

    points.append((x, y))


# Input reference point
xr = int(input("Enter reference x: "))
yr = int(input("Enter reference y: "))

reference = (xr, yr)

# Sort and print
print("Points sorted by distance:")
print(sort_by_distance(points, reference))
