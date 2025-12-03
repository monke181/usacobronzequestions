#https://usaco.org/index.php?page=viewproblem2&cpid=639
#wants to sort diamonds, will not include 2 diamonds if their size differ by more than K. find maximum number of diamonds she can display

n, k = 5, 3 #n diamonds, difference K
n_list = [] #list of diamonds 
for i in range(n): #loop thru N diamonds
    n_list.append(int(input())) #add to list
sorted_list = sorted(n_list) #sort numerically
start = 0 #2 pointers strat
end = n - 1 
max_count = 0
for end in range(n): #from end to N
    while sorted_list[end] - sorted_list[start] > k: #subtract sorted_list[end] from sorted_list index k / 2pointers method
        start += 1 #if greater than k, add to start
    count = end - start + 1 #number of diamonds currently working
    max_count = max(max_count, count)
print(max_count)