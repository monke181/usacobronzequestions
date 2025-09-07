N = 6
cities_data = [
    ["MIAMI", "FL"],
    ["DALLAS", "TX"],
    ["FLINT", "MI"],
    ["CLEMSON", "SC"],
    ["BOSTON", "MA"],
    ["ORLANDO", "FL"]
]

matches = 0
for i in range(N):
    match_word_1 = cities_data[i][0][:2]
    match_word_1_state = cities_data[i][1]
    for j in range(N):
        if i == j:
            continue
        match_word_2 = cities_data[j][0][:2]
        match_word_2_state = cities_data[j][1]
        if match_word_1 == match_word_2_state and match_word_2 == match_word_1_state:
            matches += 1
matches //= 2
print(matches)
    
matches = 0