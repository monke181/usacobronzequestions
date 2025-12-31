#https://usaco.org/index.php?page=viewproblem2&cpid=713

with open('usaco python/xInput/cowcross3.in', 'r') as read:
    N = int(read.readline()) 
    times = []  
    for _ in range(N):
        arrival, duration = map(int, read.readline().split())
        times.append((arrival, duration))

times.sort()
current_time = 0
for arrival, duration in times:
    if arrival > current_time:
        current_time = arrival
    current_time = current_time + duration
print(current_time)