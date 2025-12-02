N = 4
cows = [1, 2, 4, 3]

answer = N - 1

for i in range(N - 2, -1, -1):
    if cows[i] < cows[i+1]:
        answer -= 1
    else:
        break
    
print(answer)