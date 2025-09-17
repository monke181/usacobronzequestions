N = 7
cow_ids = [11, 2, 17, 13, 1, 15, 3]

even_count = 0
odd_count = 0
max_groups = 0
for id in cow_ids:
    if id % 2 == 0:
       even_count += 1
    else:
        odd_count += 1 
        
while odd_count > even_count:
    odd_count -= 2 
    even_count += 1
    
if even_count > odd_count + 1:
    even_count = odd_count + 1
    
max_groups = even_count + odd_count
print(max_groups)