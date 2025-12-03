#https://usaco.org/index.php?page=viewproblem2&cpid=1445
#needs

N = 3
F = 1
S = "ooo"

moo_count = {}

letters = "abcdefghijklmnopqrstuvwxyz"

all_moos = []
for ci in letters:
    for cj in letters:
        if ci != cj:
            all_moos.append(ci + cj + cj)

result = set()

for moo in all_moos:
    count = 0            
    for i in range(len(S) - 2):
        if S[i:i+3] == moo:
            count += 1
    if count >= F:
        result.add(moo)


for pos in range(N):
    for new_char in letters:
        if S[pos] == new_char:
            continue
        corrupted = S[:pos] + new_char + S[pos+1:]

        for moo in all_moos:
            count = 0
            for i in range(len(corrupted) - 2):
                if corrupted[i:i+3] == moo:
                    count += 1
                if count >= F:
                    result.add(moo)

result = sorted(result)
print(len(result))
for moo in result:
    print(moo)

#find combinations of moo
#add to dictionary
#if frequency > 2 print 