N = 4
log = [-1, -1, -1, 1]

min_day = 0
max_day = 0
is_consistent = True
log[0] == 0
expected_val = -1
for i in range(N - 1, -1, -1):
    if expected_val != -1:
        if log[i] != -1 and log[i] != expected_val:
            is_consistent = False
            break
        if log[i] == -1:
            log[i] = expected_val
    if log[i] != -1:
        expected_val = log[i]

    if expected_val > -1:
        expected_val -= 1
if is_consistent:
    min_day = 0
    potential_breakouts = 0
    
    for val in log:
        if val == 0:
            min_day += 1
        elif val == -1:
            potential_breakouts += 1

    max_day = min_day + potential_breakouts

print(max_day)