with open('usaco python/xInput/cowsignal.in', 'r') as read:
    N, M, K = map(int, read.readline().split())  # N = rows, M = cols

    original_signal = []
    for _ in range(N):
        line = read.readline().strip()
        original_signal.append(line)

with open('cowsignal.out', 'w') as out:
    for row in original_signal:
        scaled_row = ""
        for i in row:
            scaled_row += i * K
        for _ in range(K):
            print(scaled_row, file=out)