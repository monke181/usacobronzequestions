#https://atcoder.jp/contests/abc202/tasks/abc202_c
with open ('usaco python/xInput/madeup.in', 'r') as read:
    N = read.readline().strip()
    N = int(N)
    line = read.readline().split()
    A = [int(item) for item in line]
    line = read.readline().split()
    B = [int(item) for item in line]
    line = read.readline().split()
    C = [int(item) for item in line]
    
frequent_a = [0] * (N+1)

for i in range(N):
    frequent_a[A[i]] += 1

frequent_bc = [0] * (N+1)
for j in range(N):
    value = B[C[j] - 1]
    frequent_bc[value] += 1

answer = 0
for x in range(1, N+1):
    answer += frequent_a[x] * frequent_bc[x]
print(answer, file=open('madeup.out', 'w'))