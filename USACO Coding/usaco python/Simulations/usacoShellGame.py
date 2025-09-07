N = 3

moves = [
    [1, 2, 1],
    [3, 2, 1],
    [1, 3, 1]
]

max_score = 0
for start_position in range (1, 4):
    pebble_location = start_position
    current_score = 0
    for cup_1, cup_2, guess in moves:
        if pebble_location == cup_1:
            pebble_location = cup_2
        elif pebble_location == cup_2:
            pebble_location = cup_1
        if pebble_location == guess:
            current_score += 1
        print(f"  Swap {cup_1}<->{cup_2}. Pebble is now at {pebble_location}. Guess was {guess}. Current score: {current_score}")
    
    max_score = max(current_score, max_score)
    print(f"--- END OF SIMULATION. Final score for this run: {current_score}. Overall max score so far: {max_score} ---\n")
print(max_score)