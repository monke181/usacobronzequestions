#https://usaco.org/index.php?page=viewproblem2&cpid=617

with open('usaco python/xInput/loadbalancing.in', 'r') as read:
    line = read.readline().split()
    N = int(line[0])
    B  = int(line[1])
    cows_pos = []

    for _ in range(N):
        line = read.readline().split()
        cows_pos.append((int(line[0]), int(line[1])))

answer = float('inf')

for i in range(N):
    a = cows_pos[i][0] + 1
    for j in range(N):
        b = cows_pos[j][1] +1
        top_r = 0
        top_l = 0
        bot_l = 0
        bot_r = 0
        
        for k in range(N):
            if cows_pos[k][0] > a and cows_pos[k][1] > b:
                top_l += 1
            elif cows_pos[k][0] < a and cows_pos[k][1] > b:
                top_r += 1
            elif cows_pos[k][0] < a and cows_pos[k][1] < b:
                bot_l += 1
            else:
                bot_r += 1
        
        m = max(max(top_l, top_r), max(bot_l,bot_r))
        answer = min(answer, m)
print(answer, file=open('loadbalancing.out', 'w')) 
        