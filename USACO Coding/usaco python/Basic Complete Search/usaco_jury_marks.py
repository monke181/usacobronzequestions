#https://codeforces.com/contest/831/problem/C
#determine number of options for the score before judges added or deducted points


K = 2 #input num of jury members
N = 2 # input of scores that are remembered

a = [-2000, -2000]
b = [3998000, 4000000]

abs_list = [] #absolute value list
for num in a: #loop thru input, and append abs() of the input
    abs_list.append(abs(num))
is_possible = set() #set, so no duplicates (not used?)

max_value = max(abs_list) #get which number is bigger


count = 0 #      min(b) - minimum of b, subtracted from max value (of A)
for num in range(min(b) - max_value, max(b) + max_value + 1): # this is to loop thru the minimum of both b nd a to the maximum of b and a
    #                               maximum of b, added to the maximum value 
    #final score is equal to original + a[i], so you add, because if it is subtraction, it will auto subtract.
    for mark in a: # loop through a, 
        if mark not in b: #if not in b, meaning that the a score not in input b? (not correct?)
            if mark + num in b: # if it is, increase count.
                count += 1
print(count)