#https://usaco.org/index.php?page=viewproblem2&cpid=1228

with open('usaco python/xInput/countliar.in', 'r') as read:
    N = int(read.readline())
    cows = []

    for _ in range(N):
        line = read.readline().split()
        cows.append((line[0], int(line[1])))

# Try all candidate positions
positions = [p for _, p in cows]

min_liars = N

for x in positions:
    liars = 0
    for t, p in cows:
        if t == "G" and x < p:
            liars += 1
        elif t == "L" and x > p:
            liars += 1
    min_liars = min(min_liars, liars)

print(min_liars)