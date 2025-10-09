N = 5
M = 6

cow_constraints = [
    (4, 1),
    (4, 2),
    (4, 3),
    (2, 5),
    (1, 2),
    (1, 5)
]

pasture_grass = [0] * (N + 1)

for current_pasture in range(1, N +1):
    print(f"Current Pastur {current_pasture}")
    
    for grass_type in range (1,5):
        print(f" Trying gradd type {grass_type}")
        
        is_valid = True
        
        for p1, p2 in cow_constraints:
            
            neighbor = 0
            if p1 == current_pasture and p2 < current_pasture:
                neighbor = p2
                
            if p2 == current_pasture and p1 < current_pasture:
                neighbor = p1
            
            if neighbor > 0:
                
                if pasture_grass[neighbor] == grass_type:
                    is_valid = False
                    break
                
    
        if is_valid:
            pasture_grass[current_pasture] = grass_type
            break
final_answer = ""
for i in range(1, N + 1):
    final_answer += str(pasture_grass[i])

print(final_answer)
            
        
        
    