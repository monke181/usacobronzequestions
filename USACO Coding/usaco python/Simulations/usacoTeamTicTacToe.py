game = [
    ['C', 'O', 'W'],
    ['X', 'X', 'O'],
    ['A', 'B', 'C'],
]

individual_cow_win = set()
two_cow_win = set()
all_lines = []

for r in range(3):
    row = [game[r][0], game[r][1], game[r][2]]
    all_lines.append(row)
    
for c in range(3):
    col = [game[0][c], game[1][c], game[2][c]]
    all_lines.append(col)

diag1 = [game[0][0], game[1][1], game[2][2]]
diag2 = [game[0][2], game[1][1], game[2][0]]
all_lines.append(diag1)
all_lines.append(diag2)

for line in all_lines:
    a, b, c = line[0], line[1], line[2]
    letters = {a, b, c}
    if len(letters) == 1:
        individual_cow_win.add(a)
    elif len(letters) == 2:
        x, y = sorted(list(letters))
        two_cow_win.add((x, y))
print(len(individual_cow_win))
print(len(two_cow_win))