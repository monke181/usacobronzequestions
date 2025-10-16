COWS = sorted([
    'Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy', 'Sue'
])
constraints = [
    ("Buttercup", "Bella"),
    ("Blue", "Bella"),
    ("Sue", "Beatrice")
]

neighbors = {cow: [] for cow in COWS}

for cow1, cow2 in constraints:
    neighbors[cow1].append(cow2)
    neighbors[cow2].append(cow1)

final_order = []
cows_added = set()

while len(final_order) < len(COWS):
    start_cow = ""
    for cow in COWS:
        if cow not in cows_added and len(neighbors[cow]) <= 1:
            start_cow = cow
            print(f"found new chain to add, starting with {start_cow}")
            break
    current_cow = start_cow
    prev_cow = ""

    while current_cow:
        print(f"-> adding: '{current_cow} to lineup")
        final_order.append(current_cow)
        cows_added.add(current_cow)
        next_cow = ""
        for neighbor in neighbors[current_cow]:  
            if neighbor != prev_cow:
                next_cow = neighbor
                break
        prev_cow = current_cow
        current_cow = next_cow
for cow in final_order:
    print(cow)