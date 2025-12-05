#https://usaco.org/index.php?page=viewproblem2&cpid=784

n = 3
lifeguards = [
    [5, 9],
    [1, 4],
    [3, 7]
]
covered = [0] * 1001

for a, b in lifeguards: # covered time slots
    for i in range(a, b):
        covered[i] += 1
    
total_covered = 0
for i in range(1001): # count how many slots are covered
    if covered[i] > 0:
        total_covered += 1

unique = [] # unique slots 
for a, b in lifeguards:
    count = 0
    for i in range(a, b):
        if covered[i] == 1:
            count += 1
    unique.append(count)    
answer = total_covered - min(unique) #find max coverage
print(answer)