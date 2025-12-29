#https://usaco.org/index.php?page=viewproblem2&cpid=1251

# with open('usaco python/xInput/cowcollege.in', 'r') as read:
#     N = int(read.readline())
#     line = read.readline().split()
#     cows = [int(item) for item in line]
    
# tuition_amount = 1
# max_cow_attending = 0
# total_money = 0
# answer = 0
# final_tuition = 0 
# for i in range(N):
#     max_cow_attending = 0
#     tuition_amount += 1
#     for j in range(N):
#         if tuition_amount <= cows[j]:
#             max_cow_attending += 1
#         total_money = tuition_amount * max_cow_attending
#         print("max cow going", max_cow_attending, "for tuition amount", tuition_amount)
#         # print("total money:", total_money, "for tuition amount", tuition_amount)
#         answer = max(answer, total_money)
#         final_tuition = max(final_tuition, tuition_amount)
    
# print(answer, final_tuition)
# above is wrong / flawed logic?

#optimized solution?
with open('usaco python/xInput/cowcollege.in', 'r') as read:
    N = int(read.readline())
    line = read.readline().split()
    cows = [int(item) for item in line]
    cows.sort()
    answer = 0
    final_tuition = 0
    for i in range(N):
        tuition_amount = cows[i]
        max_cow_attending = N- i  
        total_money = tuition_amount * max_cow_attending
        
        if total_money > answer:
            answer = total_money
            final_tuition = tuition_amount
        elif total_money == answer:
            final_tuition = min(final_tuition, tuition_amount)
print(answer, final_tuition)