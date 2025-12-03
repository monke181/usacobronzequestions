#https://usaco.org/index.php?page=viewproblem2&cpid=1060
#takes photos form flower i to flower j. some photos have average flower (flower that has P petals). find how many photos are an average flower.
n = int(input()) #N flowers
flowers = list(map(int, input().split())) 


max_valid_photos = 0
#loop thru N flowers
for i in range(n):
    for j in range(i, n): #nested for loops/ end index of photo
        current_photo_list = flowers[i:j + 1] #get flowers (inclusive) from start index (i) to end index (j)
        average = sum(current_photo_list) / (j - i + 1) #find average petals in the picture.
        for flower in current_photo_list: #loop through current photo list, to find if flower is inside the subarray.
            if flower == average: #if flower is average, add to list
                max_valid_photos += 1
                break
print(max_valid_photos)