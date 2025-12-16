with open('usaco python/xInput/photo.in', 'r') as read:
    N = int(read.readline().strip())
    string = read.readline().strip()

pairs = []
for i in range(0, N, 2):
    pair = string[i] + string[i+1]
    if pair == "GH" or pair == "HG":
        pairs.append(pair)
ans = 0 
target = "HG"

for pair in reversed(pairs):
    if pair != target:
        ans += 1   
        if target == "HG":
            target = "GH"
        else:
            target = "HG"
        
print(ans)