#https://usaco.org/index.php?page=viewproblem2&cpid=591

with open('usaco python/xInput/pcount.in', 'r') as read:
    bronze = read.readline().split()
    silver = read.readline().split()
    gold = read.readline().split()
    platinum = read.readline().split()
    full = bronze + silver + gold +platinum
    
#gold -> plat
promotions_to_platinum = int(platinum[1]) - int(platinum[0])
# silver - gold 
gold_or_better_after = int(gold[1]) + int(platinum[1])
gold_or_better_before = int(gold[0]) + int(platinum[0])
promotions_to_gold = gold_or_better_after - gold_or_better_before

#bronze - silver
silver_or_better_after = int(silver[1]) + int(gold[1]) + int(platinum[1])
silver_or_better_before = int(silver[0]) + int(gold[0]) + int(platinum[0])
promotions_to_silver = silver_or_better_after - silver_or_better_before


print(promotions_to_silver,promotions_to_gold, promotions_to_platinum)
