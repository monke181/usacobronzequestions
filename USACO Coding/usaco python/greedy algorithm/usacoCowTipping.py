N = 3

cows = [
    [0, 0, 1],
    [1, 1, 1],
    [1, 1, 1]
]

count = 0
def flip_rectangle(end_row, end_col, grid):
    for r in range(end_row + 1):
        for c in range(end_col + 1):
            grid[r][c] = 1 - grid[r][c]
        
    

for r in range(N - 1, -1, -1):
    for c in range(N - 1, -1, -1):
        if cows[r][c] == 1:
            count += 1
            flip_rectangle(r, c, cows)

print(count)