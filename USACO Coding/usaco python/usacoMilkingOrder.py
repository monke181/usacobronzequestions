#https://usaco.org/index.php?page=viewproblem2&cpid=832

with open ('usaco python/xInput/morder.in', 'r') as read:
    line = read.readline().split()    
    N = int(line[0])
    M = int(line[1])
    K = int(line[2])
    hierarchy = read.readline().split()
    k_order = [list(map(int, read.readline().split())) for _ in range(K)]
initial_list = list(range(1, N + 1))
changed_list = list(range(1, N + 1))
def change(order, i1, j1, i2, j2):
    order[i1][j2], order[j1][i1] = order[j1][i1], order[i1][j2]
    return order
# for i in range(len(k_order)):
#     change(changed_list, k_order[i-1][i], k_order[i-1][i])
# # print(k_order[0][0])
# # print(k_order[0][1])
# # print(k_order[1][0])
# # print(k_order[1][1])
# print(changed_list)
change(changed_list, k_order[0], k_order[0], k_order[1], k_order[1])


# with open('usaco python/xInput/morder.in', 'r') as read:
#     N, M, K = map(int, read.readline().split())
#     hierarchy = list(map(int, read.readline().split())) if M > 0 else []
#     observations = []
#     for _ in range(K):
#         c, p = map(int, read.readline().split())
#         observations.append((c, p))

# def can_place(position, hierarchy, N):
#     """Check if we can complete the ordering respecting hierarchy"""
    
#     # Check: hierarchy cows with fixed positions must be in correct order
#     fixed_in_hierarchy = []
#     for i, cow in enumerate(hierarchy):
#         if position[cow] > 0:
#             fixed_in_hierarchy.append((position[cow], i))
    
#     fixed_in_hierarchy.sort()
#     for i in range(1, len(fixed_in_hierarchy)):
#         if fixed_in_hierarchy[i][1] <= fixed_in_hierarchy[i-1][1]:
#             return False
    
#     # Collect all used positions
#     used_positions = set()
#     for i in range(1, N + 1):
#         if position[i] > 0:
#             used_positions.add(position[i])
    
#     # Try to assign positions to all hierarchy cows
#     hierarchy_positions = [0] * len(hierarchy)
#     for i, cow in enumerate(hierarchy):
#         if position[cow] > 0:
#             hierarchy_positions[i] = position[cow]
    
#     # Fill in the gaps - we need to place unfixed hierarchy cows
#     available = [p for p in range(1, N + 1) if p not in used_positions]
#     available.sort()
    
#     avail_idx = 0
#     for i in range(len(hierarchy)):
#         if hierarchy_positions[i] == 0:
#             # Need to assign a position
#             min_pos = 1
#             # Must come after all previous hierarchy cows
#             for j in range(i):
#                 if hierarchy_positions[j] > 0:
#                     min_pos = max(min_pos, hierarchy_positions[j] + 1)
            
#             max_pos = N
#             # Must come before all subsequent hierarchy cows
#             for j in range(i + 1, len(hierarchy)):
#                 if hierarchy_positions[j] > 0:
#                     max_pos = min(max_pos, hierarchy_positions[j] - 1)
            
#             # Find first available position in range
#             found = False
#             temp_idx = avail_idx
#             while temp_idx < len(available):
#                 if min_pos <= available[temp_idx] <= max_pos:
#                     hierarchy_positions[i] = available[temp_idx]
#                     avail_idx = temp_idx + 1
#                     found = True
#                     break
#                 temp_idx += 1
            
#             if not found:
#                 return False
    
#     return True

# answer = N

# for k in range(K + 1):
#     for pos in range(1, N + 1):
#         position = [0] * (N + 1)
        
#         # Apply first k observations
#         valid = True
#         for i in range(k):
#             cow, p = observations[i]
#             if position[cow] != 0 and position[cow] != p:
#                 valid = False
#                 break
#             position[cow] = p
        
#         if not valid:
#             continue
        
#         # Try placing cow 1 at position pos
#         if position[1] != 0 and position[1] != pos:
#             continue
#         position[1] = pos
        
#         # Check if this placement is valid
#         if can_place(position, hierarchy, N):
#             answer = pos
#             break
    
#     if answer < N:
#         break

# with open('morder.out', 'w') as write:
#     write.write(str(answer) + '\n')