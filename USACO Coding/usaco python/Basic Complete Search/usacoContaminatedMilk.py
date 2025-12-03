#https://usaco.org/index.php?page=viewproblem2&cpid=569
#exactly one of M type of milk has gone bad, john does not know which one

#input gives who drinks what, when each person gets sick, find the sick one
#john needs amount of doses of medicine he needs to guarantee he can cure the sick people

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

max_doses_needed =  0 #count of doses
for candidate_milk in range(1, M + 1): #loop from 1 through M + 1 types of milk
    
    is_possible_milk = True #assume that milk has gone bad?
    
    for sick_person, sick_time in sick_events: #loop through sick events list
        drank_before_sick = False #bool / flag
        for p, m, t in drink_events: #loop thru drink events 
            if p == sick_person and m == candidate_milk and t < sick_time: #if p matches up wit sick person, m = the index of the milk (from loop)
                drank_before_sick = True #flag true
                break
            
        if not drank_before_sick: # if false
            is_possible_milk = False #not spoiled milk
            break
        
    if is_possible_milk: #if milk gone bad?
        people_who_drank_this = set() #no duplicates list of people who drank
        for p, m, t in drink_events: #loop thru drink events
            if m == candidate_milk: #once hits on spoiled milk, add to list
                people_who_drank_this.add(p)
                
        max_doses_needed = max(len(people_who_drank_this), max_doses_needed) #minimum amount of doses, of list and of itself
print(max_doses_needed)