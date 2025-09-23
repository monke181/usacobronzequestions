N = 6
heights_of_cows = [2,4,7,7,9,3]

copy_of_heights = []

count = 0
for i in range(N):
    copy_of_heights.append(heights_of_cows[i])
copy_of_heights.sort()
 
for i in range(N):
    if copy_of_heights[i] != heights_of_cows[i]:
        count += 1
print(count - 1)