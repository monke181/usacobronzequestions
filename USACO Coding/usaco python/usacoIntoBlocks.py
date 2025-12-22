#https://codeforces.com/problemset/problem/1209/G1?mobile=false

with open('usaco python/xInput/iblocks.in', 'r') as read:
    line = read.readline()
    N = int(line[0])
    Q = 0
    line = read.readline().split()
    initial_sequence = [int(item) for item in line]


def initial_check(N, sequence):
    flag = False
    seen = set()
    previous = sequence[0]
    seen.add(previous)
    for i in range(1, N):
        if sequence[i] == previous:
            continue
        elif sequence[i] in seen:
            flag = True
            break
        else:
            seen.add(sequence[i])
            previous = sequence[i]
            
    return flag

if initial_check(N, initial_sequence) == False:
    print(0)
counts = {}
for s in initial_sequence:
    if s in counts:
        counts[s] += 1
    else:
        counts[s] = 1
min_key = None
min_value = None
for key, value in counts.items():
    if min_value is None or value < min_value:
        min_value = value
        min_key = key
        
print(min_value)