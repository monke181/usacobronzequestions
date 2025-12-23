with open('usaco python/xInput/mooloo.in', 'r') as read:
    line = read.readline().split()
    N = int(line[0])
    K = int(line[1])
    line = read.readline().split()
    n_days = [int(item) for item in line]
    
cost = K + 1
for i in range(1, N):
    gap = n_days[i] - n_days[i-1]
    cost = cost + min(gap, K+1)
print(cost)