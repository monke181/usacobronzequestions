N = 4  
M = 3

raw_cards = [
    [1,2,3],
    [3,2,1],
    [1,2,1],
    [4,2,7]
]
pairs = []

running_sum = 0

for i in range(N):
    for j in range(N):
        if not i == j and not pairs.count((j,i)) >= 1:
            pairs.append((i,j))
            for card in range(M):
                running_sum += abs(raw_cards[i][card] - raw_cards[j][card])
print(running_sum)