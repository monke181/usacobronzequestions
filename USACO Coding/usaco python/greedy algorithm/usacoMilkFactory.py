N = 3
walkways = [
    (1, 2),
    (3, 2)
]

nums = {}

for walk in walkways:
    if walk[1] not in nums.keys():
        nums[walk[1]] = 1
    else:
        nums[walk[1]] += 1

max_key = max(nums, key=nums.get)
if nums[max_key] == N - 1:
    print(max_key)
else:
    print("-1")
