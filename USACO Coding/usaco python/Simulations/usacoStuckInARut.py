N = 6
starting_location = [
    ("E", 3, 5),
    ("N", 5, 3),
    ("E", 4, 6),
    ("E", 10, 4),
    ("N", 11, 2),
    ("N", 8, 1),
]

# Separate cows by direction
north = []
east = []
for i, (d, x, y) in enumerate(starting_location):
    if d == "N":
        north.append((x, y, i))
    else:
        east.append((x, y, i))

# Sort north cows by x (left to right)
north.sort(key=lambda c: c[0])
# Sort east cows by y (bottom to top)
east.sort(key=lambda c: c[1])

INF = 10**9
stopped = [INF] * N  # distance traveled before stopping

# Simulate interactions
for ex, ey, ei in east:
    for nx, ny, ni in north:
        # Intersection only possible if east cow is left and north cow is below
        if ex < nx and ny < ey:
            east_time = nx - ex
            north_time = ey - ny

            # If east cow reaches later and north not stopped before intersection
            if east_time < north_time and stopped[ni] > north_time:
                stopped[ni] = north_time
            # If north cow reaches later and east not stopped before intersection
            elif north_time < east_time and stopped[ei] > east_time:
                stopped[ei] = east_time

# Print results
for dist in stopped:
    if dist == INF:
        print("Infinity")
    else:
        print(dist)