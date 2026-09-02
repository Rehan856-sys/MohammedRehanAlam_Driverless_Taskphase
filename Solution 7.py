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


points = [(0, 1), (0, 3), (1, 2)]

xr = int(input("Enter reference x: "))
yr = int(input("Enter reference y: "))

reference = (xr, yr)

print(sort_by_distance(points, reference))