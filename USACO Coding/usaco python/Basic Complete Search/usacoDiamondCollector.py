n, k = 5, 3
n_list = []
for i in range(n):
    n_list.append(int(input()))
sorted_list = sorted(n_list)
start = 0
end = n - 1
max_count = 0
for end in range(n):
    while sorted_list[end] - sorted_list[start] > k:
        start += 1
    count = end - start + 1
    max_count = max(max_count, count)
print(max_count)