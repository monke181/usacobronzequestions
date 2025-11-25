test_cases = [
    (6, [1, 2, 3, 1, 1, 1]),
    (3, [2, 2, 3]),         
    (5, [0, 0, 0, 0, 0])
]

result = 0
for n, period in test_cases:
    total_sum = sum(period) #get sum
    
    if total_sum == 0: #if 0, everything 0
        result = 0
        print(result)
        break

    result = n -1 # if not divisible
        
    for num_groups in range(n, 0, -1):
        if total_sum % num_groups != 0:
            continue
        target_val = total_sum // num_groups
    
        total = 0
        group_formed = 0
        
        for i in period:
            total += i
            if total == target_val:
                group_formed += 1
                total = 0
            elif total > target_val:
                break
        if group_formed == num_groups:
            result = n - num_groups
            break
                
    print(result)
            #if not divisible by itself, it will be n - 1
            # 2 loops add up to every combination.
            # what is target sum?
            # pick a num of groups (num_groups)
            # figure what group should sum to (target_val) (group_sum)
            #try to make groups, try to equal target val
            # split into exactly num_groups
            #answer is n - num_groups