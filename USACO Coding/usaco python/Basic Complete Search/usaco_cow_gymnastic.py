#https://usaco.org/index.php?page=viewproblem2&cpid=963
# getting consistency of cows


#Inputs
K = 3 # num of sessions
N = 4 # num of cows

all_sessions = [
    [4, 1, 2, 3], 
    [4, 1, 3, 2],
    [4, 2, 1, 3]
]


#function, gets a pair of cows, as well as range of rankings
def find_consistency(cow_a, cow_b, practice):
    point_a = -1 #stores cow a position
    point_b = -1 #stores cow b position in ranking 
    for i in range(N): #loop thru num of cows
        if practice[i] == cow_a:
            point_a = i #index means cows position
        if practice[i] == cow_b:
            point_b = i
    return point_a < point_b #return cow a if index is smaller

final_count = 0

#loop through all cows                
for cow_x in range(1, N + 1):
    for cow_y in range(1, N + 1): #nested for loop thru all cows
        count = 0  
        for cow_session in all_sessions: #loop thru sessions out of sessions
            if find_consistency(cow_x, cow_y, cow_session): # if cow a index smaller, it returns true, thus adding 1
                count += 1
        if count == 3: #if cow is consistent 3 times, add to final count
            final_count += 1
print(final_count)
        