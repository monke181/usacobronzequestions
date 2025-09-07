COW_NAMES = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]

cow_milk_totals = [0] * len(COW_NAMES)

log_entries = [
    ["Bessie", 1],
    ["Maggie", 13],
    ["Elsie", 3],
    ["Elsie", 4],
    ["Henrietta", 4],
    ["Gertie", 12],
    ["Daisy", 7],
    ["Annabelle", 10],
    ["Bessie", 6],
    ["Henrietta", 5]
]

#cow_index = COW_NAME.index("Maggie")
#prints index of cow
        
for entry in log_entries:
    cow, milk = entry
    cow_index = COW_NAMES.index(cow)
    cow_milk_totals[cow_index] += milk

cow_milk_totals = sorted(cow_milk_totals)
smallest_val = min(cow_milk_totals)
second_smallest = 0
for i in range(len(cow_milk_totals)):
    if cow_milk_totals[i] == smallest_val:
        continue
    elif cow_milk_totals[i] < smallest_val:
        second_smallest = i
        break
    

print(COW_NAMES[second_smallest])
# cands = []
# for i in range(len(cow_milk_totals)):
#     if cow_milk_totals[i] == second_smallest:
#         cands.append(COW_NAMES[i])
        
        
# if len(cands) == 1:
#     print(cands[0])
# else:
#     print("Tie")