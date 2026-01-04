with open('usaco python/xInput/measuretraffic.in', 'r') as read:
    N = int(read.readline().strip())
    
    segments = []
    for _ in range(N):
        seg_type, L, R = read.readline().split()
        segments.append((seg_type, int(L), int(R)))

low = 0
high = float('inf')

for i in range(N):
    type, L, R = segments[i]

    if type == "on":
        low += L
        high += R
    elif type == "off":
        low -= R
        high -= L
    else:  
        low = max(low, L)
        high = min(high, R)

final_low = low
final_high = high
low = final_low
high = final_high

for i in range(N - 1, -1, -1):
    type, L, R = segments[i]

    if type == "on":
        low -= L
        high -= R
    elif type == "off":
        low += L
        high += R
    else: 
        low = max(low, L)
        high = min(high, R)

start_low = low
start_high = high

with open('measuretraffic.out', 'w') as write:
    print(start_low, start_high, file=write)
    print(final_low, final_high, file=write)