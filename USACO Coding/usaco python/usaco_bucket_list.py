start_times = { 2: 2, 4: 1, 8: 3 }
end_times   = { 6: 2, 10: 1, 13: 3 }

buckets_used = 0
max_buckets = 0

for time in range(15):
    if time in start_times:
        buckets_used += start_times[time]
    if time in end_times:
        max_buckets = max(buckets_used, max_buckets)
        buckets_used -= end_times[time]
print(max_buckets)
        
        