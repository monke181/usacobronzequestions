measurements = [
    (7, "Mildred", 3),
    (4, "Elsie", -1),
    (9, "Mildred", -1),
    (1, "Bessie", 2)
]

milk_outputs = {
    "Bessie": 7,
    "Elsie": 7,
    "Mildred": 7
}

display_changes = 0 
current_display = ["Bessie", "Elsie", "Mildred"]

measurements.sort()

for day, cow_name, milk_change in measurements:
    milk_outputs[cow_name] += milk_change
    max_output = max(milk_outputs.values())

    new_display = []
    for cow in milk_outputs:
        if milk_outputs[cow] == max_output:
            new_display.append(cow)
    
    if current_display != new_display:
        display_changes += 1 
    current_display = new_display
print(display_changes)