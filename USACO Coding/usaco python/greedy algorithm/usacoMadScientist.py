N = 7
A = "GHHHGHH"
B = "HHGGGHH"

count = 0
flag = False
for i in range(N):
    seg1 = A
    seg2 = B
    if A[i] != B[i] and not flag:
        count += 1
        flag = True
    if A[i] == B[i]:
        flag = False
print(count)