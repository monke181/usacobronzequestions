# https://usaco.org/index.php?page=viewproblem2&cpid=760

# with open('usaco python/xInput/bovineshuffle.in', 'r') as read:
#     N = int(read.readline())

#     order = list(map(int, read.readline().split()))
#     cows = list(map(int, read.readline().split()))

#     shuffle_order = {}
#     for cow, idx in zip(cows, order):
#         shuffle_order[cow] = idx
        

# # shuffle_order[1234567] == 1

# array = [[0]*7 for _ in range(N)]
# for i in range(N):
#    for key, value in shuffle_order.items():
#        if value == i:
#            array[i] += shuffle_order[key]
           
# print(array) 
#flawed logic
    
with open('usaco python/xInput/bovineshuffle.in', 'r') as f:
    N = int(f.readline())
    a = [x - 1 for x in map(int, f.readline().split())]
    cows = list(map(int, f.readline().split()))

# Reverse the shuffle 3 times
for _ in range(3):
    prev = [0] * N
    for i in range(N):
        prev[i] = cows[a[i]]
    cows = prev

with open('shuffle.out', 'w') as f:
    for cow in cows:
        f.write(str(cow) + '\n')