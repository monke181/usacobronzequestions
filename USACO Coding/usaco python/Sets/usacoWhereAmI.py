n = 7
s = "ABCDABC"


def check_for_duplicates(current_k):
    seen = set()
    for i in range(n - current_k + 1):
        substring = s[i:i+current_k]
        if substring in seen:
            return True
        seen.add(substring)
    return False

k = 1
while True:
    if not check_for_duplicates(k):
        break
    else:
        k += 1
print(k)
