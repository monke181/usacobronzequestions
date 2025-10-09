N = 4

pathways = [
    (1, 2),
    (4, 3),
    (2, 3),
]
list_of_degrees = [0] * (N + 1)

for field1, field2 in pathways:
    list_of_degrees[field1] = list_of_degrees[field1] + 1
    list_of_degrees[field2] = list_of_degrees[field2] + 1
min_grass = max(list_of_degrees) + 1

print(min_grass)

