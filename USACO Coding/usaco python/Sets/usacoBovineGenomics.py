N = 3
M = 8

spotty = ["AATCCCAT", "GATTGCAA", "GGTCGCAA"]
plain  = ["ACTCCCAG", "ACTCGCAT", "ACTTCCAT"]

count = 0
for i in range(M):
    spotty_cow = set()
    reg_cow = set()
    for genome1 in spotty:
        spotty_cow.add(genome1[i])
    for genome2 in plain:
        reg_cow.add(genome2[i]) 
    if spotty_cow.isdisjoint(reg_cow):
        count += 1
print(count)