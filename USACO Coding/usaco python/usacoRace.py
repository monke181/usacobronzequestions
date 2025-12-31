# with open('usaco python/xInput/race.in', 'r') as read:
#     line = read.readline().split()
#     K = int(line[0])
#     N = int(line[1])
#     X = []
#     for _ in range(N):
#         line = read.readline().strip()
#         X.append(int(line))

# def calculate_min_time(K, X):
#     t = 1
#     while True:
#         max_s = min(t, X + (t - X)//2) 
#         acceleration = max_s * (max_s + 1) // 2
#         deceleration = (max_s - X) * (max_s - X + 1) // 2
#         cruise = t - (max_s + (max_s - X))
#         if cruise < 0:
#             cruise = 0
#         cruise_dist = cruise * max_s
#         total_dist = acceleration + deceleration + cruise_dist
#         if total_dist >= K:
#             return t
#         t += 1

# for i in X:
#     print(calculate_min_time(K, i))

with open('usaco python/xInput/race.in', 'r') as read:
    line = read.readline().split()
    K = int(line[0])
    N = int(line[1])
    X_list = []
    for _ in range(N):
        line = read.readline().strip()
        X_list.append(int(line))

def calculate_min_time(K, X):
    dist = 0
    speed = 0
    time = 0
    
    while dist < K:
        time += 1
        
        # Calculate remaining distance
        remaining = K - dist
        
        # Check if we can finish by accelerating and then decelerating to X
        # If we go to speed (speed+1), distance to decelerate to X:
        if speed + 1 <= X:
            # We're still below or at X, safe to accelerate
            speed += 1
        else:
            # We're above X, check if we need to decelerate
            # Distance needed to decelerate from current speed to X
            decel_needed = (speed - X) * (speed + X + 1) // 2
            
            if decel_needed >= remaining:
                # We need to start decelerating now
                speed -= 1
            else:
                # We can still accelerate
                speed += 1
        
        dist += speed
    
    return time

with open('race.out', 'w') as write:
    for x in X_list:
        write.write(str(calculate_min_time(K, x)) + '\n')