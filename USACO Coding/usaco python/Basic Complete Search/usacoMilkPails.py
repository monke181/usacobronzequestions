#https://usaco.org/index.php?page=viewproblem2&cpid=615
#needs to fill milk w three mails of size X Y M. all pails are empty at the start
# can perform 2 operations: fill the smallest pail (size X) fully, and pour into M pail, as long as M pail doesn't overflow
#or can fill medium pail (size Y) completely to the top and pour into size M pail, as long as M pail doesn't overflow.

X, Y, M = 17, 25, 77 #size of pails
max_x = M // X #max num of times we can use size X pail without overflowing
max_y = M // Y  #num of times we can use size Y pail without overflowing
answer = 0

#if x or y can perfectly fill M, then the answer is that
if (max_x * X == M) or (max_y * Y == M):
    answer = M
else:
    best = 0
    for i in range(1, max_x + 1):  #loop through from 1 to maximum times + 1
        j = 0
        while i * X + j * Y <= M:    #try every Y pours that still fits into M
            best = max(best, i * X + j * Y) #update closest valid amound
            j += 1
answer = best 
    
    

print(answer)