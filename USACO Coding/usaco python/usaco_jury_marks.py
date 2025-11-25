K = 2
N = 2

a = [-2000, -2000]
b = [3998000, 4000000]

abs_list = []
for num in a:
    abs_list.append(abs(num))
is_possible = set()

max_value = max(abs_list)


count = 0
for num in range(min(b) - max_value, max(b) + max_value + 1):
    for mark in a:
        if mark not in b:
            if mark + num in b:
                print(num)
                count += 1
print(count)