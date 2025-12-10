#https://codeforces.com/problemset/problem/863/B

with open('usaco python/xInput/kayaking.in', 'r') as read:
    N = read.readline()
    N = int(N)
    list = read.readline().split()
    weight = [int(item) for item in list]

min_instability = float('inf')
for i in range(N*2):
    for j in range(i + 1, N*2):
        tandem_riders = []
        for k in range(N * 2):
            if k != i and k != j:
                tandem_riders.append(weight[k])
        current_instability = 0
        for index in range(0, len(tandem_riders), 2):
            current_instability += abs(tandem_riders[index] - tandem_riders[index + 1])
        min_instability = min(min_instability, current_instability)
print(min_instability)