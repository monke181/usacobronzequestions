X, Y, M = 17, 25, 77
max_x = M // X
max_y = M // Y
answer = 0

if (max_x * X == M) or (max_y * Y == M):
    answer = M
else:
    best = 0
    for i in range(1, max_x + 1): 
        j = 0
        while i * X + j * Y <= M:   
            best = max(best, i * X + j * Y)
            j += 1
answer = best 
    
    

print(answer)