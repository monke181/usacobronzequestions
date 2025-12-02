N = 4
points = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 2)
]
max_area = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            base = 0
            height = 0
            if points[i][0] == points[k][0] and points[i][1] == points[j][1]:
                base = abs(points[i][0] - points[j][0])
                height = abs(points[i][1] - points[k][1])
                
                area = (base * height) // 2
                max_area = max(max_area, area)
print(max_area * 2)
    