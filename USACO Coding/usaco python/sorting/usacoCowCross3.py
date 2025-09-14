N = 3
cows = [
    [2, 1],
    [8, 3],
    [5, 7]
]
cows.sort()
current_final_time = 0
for start, process_time in cows:
    start_time = max(current_final_time, start)
    current_final_time = start_time + process_time
    
print(current_final_time)