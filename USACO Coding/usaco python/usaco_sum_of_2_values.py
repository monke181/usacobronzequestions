x = 8

a = [2, 7, 5, 1]

n = 4 

key_value = {}

for i in range(n):
    key = x - a[i]
    if key not in key_value:
        key_value[a[i]] = i
    else:
        print(key_value[key], i) 