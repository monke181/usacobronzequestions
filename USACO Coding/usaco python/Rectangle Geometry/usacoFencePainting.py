import random

johnA = random.randint(0, 100)
johnB = random.randint(johnA + 1, 100)
bessieC = random.randint(0, 100)
bessieD = random.randint(bessieC + 1, 100)

john = johnB - johnA
bessie = bessieD - bessieC
sumx = john + bessie
overlap = max(0, min(johnB, bessieD) - max(johnA, bessieC))
sumx -= overlap

print(johnA, johnB, bessieC, bessieD)
print(sumx)