N = 4
original_log = [-1, -1, -1, 1]

def check_consistency_and_count(log_input, mode):
    """
    mode: 'min' - replace -1 with largest possible value
          'max' - try to maximize breakouts by replacing -1 with 0 when possible
    """
    log = log_input[:]
    log[0] = 0  # Day 0 must be a breakout
    
    if mode == 'min':
        # For minimum: going backwards, fill -1s with required values
        expected_val = -1
        for i in range(N - 1, -1, -1):
            if expected_val != -1:
                if log[i] != -1 and log[i] != expected_val:
                    return None  # Inconsistent
                if log[i] == -1:
                    log[i] = expected_val
            
            if log[i] != -1:
                expected_val = log[i]
            
            if expected_val > -1:
                expected_val -= 1
        
        # Count breakouts (where log[i] == 0)
        return sum(1 for x in log if x == 0)
    
    else:  # mode == 'max'
        # For maximum: try to place as many breakouts as possible
        # Go forward and greedily make -1s into 0s when valid
        for i in range(N):
            if log[i] == -1:
                log[i] = 0  # Try to make it a breakout
        
        # Now validate by going backwards
        expected_val = -1
        for i in range(N - 1, -1, -1):
            if expected_val != -1:
                if log[i] != expected_val:
                    return None  # Inconsistent
            
            if log[i] == 0:
                expected_val = -1  # Reset after a breakout
            else:
                expected_val = log[i]
            
            if expected_val > -1:
                expected_val -= 1
        
        return sum(1 for x in log if x == 0)

# Check consistency first with min approach
min_count = check_consistency_and_count(original_log, 'min')

if min_count is None:
    print(-1)
else:
    max_count = check_consistency_and_count(original_log, 'max')
    print(f"{min_count} {max_count}")

# Debug
log_test = original_log[:]
log_test[0] = 0
print(f"Original: {original_log}")
print(f"After min fill: ", end="")
check_consistency_and_count(original_log, 'min')