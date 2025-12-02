#import sys
#N_rooms = sys.stdin.readline()


with open('usaco python/cbarn.in') as read:
    N_rooms = int(read.readline())
    rooms = [ int(read.readline()) for _ in range(N_rooms)]


minimum_distance = float('inf')
for j in range(N_rooms): 
    total_sum = 0
    for i in range (N_rooms):
        room_index = (j + i ) % N_rooms
        total_sum += rooms[room_index] * i
    minimum_distance = min(minimum_distance, total_sum)
print(minimum_distance, file=open('cbarn.out', 'w'))
