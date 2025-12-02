K = 3
N = 4

all_sessions = [
    [4, 1, 2, 3], 
    [4, 1, 3, 2],
    [4, 2, 1, 3]
]
def find_consistency(cow_a, cow_b, practice):
    point_a = -1
    point_b = -1
    for i in range(4):
        if practice[i] == cow_a:
            point_a = i
        if practice[i] == cow_b:
            point_b = i
    return point_a < point_b

final_count = 0
                
for cow_x in range(1, N + 1):
    for cow_y in range(1, N + 1):
        count = 0 
        for cow_session in all_sessions:
            if find_consistency(cow_x, cow_y, cow_session):
                count += 1
        if count == 3:
            final_count += 1
print(final_count)
        