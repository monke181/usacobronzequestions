N, M, D, S = 3, 4, 7, 2

drink_events = [
    [1, 1, 1], [1, 4, 1], 
    [1, 3, 4], [1, 2, 2],
    [3, 1, 3], [2, 1, 5], [2, 2, 7]
]

sick_events = [
    [1, 3],
    [2, 8]
]

max_doses_needed =  0
for candidate_milk in range(1, M + 1):
    
    is_possible_milk = True
    
    for sick_person, sick_time in sick_events:
        drank_before_sick = False
        for p, m, t in drink_events:
            if p == sick_person and m == candidate_milk and t < sick_time:
                drank_before_sick = True
                break
            
        if not drank_before_sick:
            is_possible_milk = False
            break
        
    if is_possible_milk:
        people_who_drank_this = set()
        for p, m, t in drink_events:
            if m == candidate_milk:
                people_who_drank_this.add(p)
                
        max_doses_needed = max(len(people_who_drank_this), max_doses_needed)
print(max_doses_needed)