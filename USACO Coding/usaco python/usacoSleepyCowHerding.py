cow_locations = [4, 7, 9]

cow_locations.sort()

a = cow_locations[0]
b = cow_locations[1]
c = cow_locations[2]

max_moves = 0
min_moves = 0
if c - a == 2:
    min_moves = 0
elif (c - b) == 2 or (b - a) == 2:
    min_moves = 1
else:
    min_moves = 2

if b - a > c-b:
    max_moves = (b - a) - 1
else:
    max_moves = (c - b) -1
print(min_moves)
print(max_moves)