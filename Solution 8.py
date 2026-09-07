import csv
import math


def distance_from_origin(cone):

    x = float(cone["x"])
    y = float(cone["y"])

    return x * x + y * y


def distance_between(cone1, cone2):

    x1 = float(cone1["x"])
    y1 = float(cone1["y"])

    x2 = float(cone2["x"])
    y2 = float(cone2["y"])

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


# Read cones.csv

cones = []

with open("cones.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        cones.append(row)


# Sort by distance from origin

cones.sort(key=distance_from_origin)


# Separate colours

blue = []
yellow = []

for cone in cones:

    if cone["colour"].lower() == "blue":
        blue.append(cone)

    elif cone["colour"].lower() == "yellow":
        yellow.append(cone)


# Write blue.csv

with open("blue.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["id", "x", "y", "colour"]
    )

    writer.writeheader()
    writer.writerows(blue)


# Write yellow.csv

with open("yellow.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["id", "x", "y", "colour"]
    )

    writer.writeheader()
    writer.writerows(yellow)


# Find midpoint for every blue cone
# and its nearest yellow cone

midpoints = []

for b in blue:

    nearest_yellow = min(
        yellow,
        key=lambda y: distance_between(b, y)
    )

    x1 = float(b["x"])
    y1 = float(b["y"])

    x2 = float(nearest_yellow["x"])
    y2 = float(nearest_yellow["y"])

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    midpoints.append(
        (midpoint_x, midpoint_y)
    )


# Write centreline.csv

with open("centreline.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["x", "y"])

    for point in midpoints:
        writer.writerow(point)


print("Files created successfully.")
