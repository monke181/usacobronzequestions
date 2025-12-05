#https://usaco.org/index.php?page=viewproblem2&cpid=1491


with open('usaco python/reflection.in') as read:
    line = read.readline()
    N, U = line.split()
    N = int(N)
    U = int(U)
    canvas = []
    for i in range(N):
        reading = read.readline()
        reading = list(reading)
        reading.pop(-1)
        canvas.append(reading)
    edits = []
    for i in range(U):
        reading = read.readline().split()
        edits.append([int(reading[0]), int((reading[1]))])
        
operations_count = 0

canvas1 = []
canvas2 = []
canvas3 = []
canvas4 = []

mid = N // 2
for x, y in edits:
    if canvas[x-1][y-1] == '#':
        canvas[x-1][y-1] = '.'
    else:
        canvas[x-1][y-1] = '#'
    
    
    def get_quadrants(canvas):
        N = len(canvas)
        mid = N // 2   # N is even per your note

        q1 = [row[0:mid]     for row in canvas[0:mid]]
        q2 = [row[mid:N]     for row in canvas[0:mid]]
        q3 = [row[0:mid]     for row in canvas[mid:N]]
        q4 = [row[mid:N]     for row in canvas[mid:N]]

        return q1, q2, q3, q4

    canvas1, canvas2, canvas3, canvas4 = get_quadrants(canvas)
    
    # def check_reflection(canvas1, canvas2):
    #     isReflection = True
    #     N = len(canvas1)
    #     for i in range(N):
    #         for j in range(N):
    #             if canvas1[i][j] != canvas2[i][N-1-j]:
    #                 return False
    #             if canvas1[i][j] != canvas2[N-1-j][i]:
    #                 return False
    #     return isReflection


        
