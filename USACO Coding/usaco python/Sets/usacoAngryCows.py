N = 6
hay_bales = [8, 5, 6, 13, 3, 4]
hay_bales.sort()
max_exploded = 0

for i in range(N):
    start_pos = hay_bales[i]
    print(f"\n--- Testing start at index {i} (position {start_pos}) ---")
    exploded_count_left = 0
    blast_radius = 1
    last_explosion_index = i
    
    while True:
        next_step_index = -1
        
        j = last_explosion_index - 1
        while j >= 0:
            distance = hay_bales[last_explosion_index] - hay_bales[j]
            if distance <= blast_radius:
                next_step_index = j
                j -= 1
            else:
                break
                
        if next_step_index == -1:
            print("left: chain reaction stopped")
            break
        else:
            num_newly_exploded = last_explosion_index - next_step_index
            exploded_count_left += num_newly_exploded
            print(f"  LEFT: Radius {blast_radius} from pos {hay_bales[last_explosion_index]} hits down to pos {hay_bales[next_step_index]}. Exploded {num_newly_exploded} more.")
            
            last_explosion_index = next_step_index
            blast_radius += 1
            
    exploded_count_right = 0
    blast_radius = 1
    last_explosion_index = i
    while True:
        next_step_index = -1
        
        j = last_explosion_index + 1
        while j < N:
            distance = hay_bales[j] - hay_bales[last_explosion_index]
            if distance <= blast_radius:
                next_step_index = j
                j += 1
            else:
                break
                
        if next_step_index == -1:
            print(f"right: chain reaction stopped")
            break
        else:
            num_newly_exploded = next_step_index - last_explosion_index
            exploded_count_right += num_newly_exploded
            print(f"  Right: Radius {blast_radius} from pos {hay_bales[last_explosion_index]} hits down to pos {hay_bales[next_step_index]}. Exploded {num_newly_exploded} more.")
            
            last_explosion_index = next_step_index
            blast_radius += 1
    current_total = exploded_count_left + exploded_count_right + 1
    print(f"  Total for this start: {current_total} (1 + {exploded_count_left} left + {exploded_count_right} right)")
    
    max_exploded = max(max_exploded, current_total)
    print(f"\nFinal Answer: The maximum number of bales that can be exploded is {max_exploded}")