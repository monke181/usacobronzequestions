N = 4
canvas = [
    [2, 2, 3, 0],
    [2, 7, 3, 7],
    [2, 7, 7, 7],
    [0, 0, 0, 0]
]

min_rows = [float('inf')] * 10
min_cols = [float('inf')] * 10

max_rows = [-1] * 10
max_cols = [-1] * 10

colors_seen = set()

for r in range(N):
    for c in range(N):
        color = canvas[r][c]
        if color != 0:
            colors_seen.add(color)
            min_rows[color] = min(min_rows[color], r)
            max_rows[color] = max(max_rows[color], r)
            
            min_cols[color] = min(min_cols[color], c)
            max_cols[color] = max(max_cols[color], c)
            
print("--- Bounding Boxes ---")
for color in sorted(list(colors_seen)):
    print(f"Color {color}: Rows {min_rows[color]}-{max_rows[color]}, Cols {min_cols[color]}-{max_cols[color]}")
print("----------------------\n")

possible_first_color = 0

for color1 in colors_seen:
    could_be_first = True
    for color2 in colors_seen:
        if color1 == color2:
            continue
        
        c2_min_r, c2_max_r = min_rows[color2], max_rows[color2]
        c2_min_c, c2_max_c = min_cols[color2], max_cols[color2]
        
        for r in range(c2_min_r, c2_max_r + 1):
            for c in range(c2_min_c, c2_max_c + 1):
                if canvas[r][c] == color1:
                    could_be_first = False
                    break
    if could_be_first:
        possible_first_color += 1
        break
print(possible_first_color)