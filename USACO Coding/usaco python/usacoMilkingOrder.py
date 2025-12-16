with open ('usaco python/xInput/morder.in', 'r') as read:
    line = read.readline().split()    
    N = int(line[0])
    M = int(line[1])
    K = int(line[2])
    
    hierarchy_str = read.readline().split()
    hierarchy = [int(c) for c in hierarchy_str]
    
    fixed_cows = {}
    for _ in range(K):
        cow_id, position = map(int, read.readline().split())
        fixed_cows[cow_id] = position - 1 

# 2. SETUP DATA STRUCTURES
# ------------------------------------------
barn = [0] * N

for cow, idx in fixed_cows.items():
    barn[idx] = cow

# 3. ALGORITHM IMPLEMENTATION
# ------------------------------------------

if 1 in hierarchy:
    
    sim_barn = list(barn) 
    current_idx = 0
    
    for cow in hierarchy:
        if cow in fixed_cows:
            current_idx = fixed_cows[cow] + 1
        else:
            while current_idx < N and sim_barn[current_idx] != 0:
                current_idx += 1
            
            if current_idx < N:
                sim_barn[current_idx] = cow
                current_idx += 1

    answer = sim_barn.index(1) + 1

else:
    
    if 1 in fixed_cows:
        answer = fixed_cows[1] + 1
    else:
        sim_barn = list(barn)

        current_idx = N - 1
        
        for i in range(len(hierarchy) - 1, -1, -1):
            cow = hierarchy[i]
            
            if cow in fixed_cows:
                current_idx = fixed_cows[cow] - 1
            else:
                while current_idx >= 0 and sim_barn[current_idx] != 0:
                    current_idx -= 1
                
                if current_idx >= 0:
                    sim_barn[current_idx] = cow
                    current_idx -= 1
        
        answer = -1
        for i in range(N):
            if sim_barn[i] == 0:
                answer = i + 1
                break
        
# 4. WRITE OUTPUT
# ------------------------------------------

try:
    with open ('morder.out', 'w') as write:
        write.write(str(answer) + '\n')
except:
    print(answer)