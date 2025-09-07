x, y = 3, 6
distance = 0
current_pos = x
step = 1
while True:
    target = x + step
    if min(current_pos, target) <= y <= max(current_pos, target):
        distance += abs(y - current_pos)
        break
    else:
        distance += abs(target - current_pos)
        current_pos = target
        step *= -2
print(distance)