n = int(input())
flowers = list(map(int, input().split()))

max_valid_photos = 0
for i in range(n):
    for j in range(i, n):
        current_photo_list = flowers[i:j + 1]
        average = sum(current_photo_list) / (j - i + 1)
        for flower in current_photo_list:
            if flower == average:
                max_valid_photos += 1
                break
print(max_valid_photos)