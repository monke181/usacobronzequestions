#https://usaco.org/index.php?page=viewproblem2&cpid=1470

with open('usaco python/xInput/ccheck.in') as read:
    N = read.readline()
    N = int(N) #N is the amount of cows
    list1 = read.readline().split() #cow order is the order of cow, get index as cowOrder[0]
    list2 = read.readline().split() #vet order is what order vet wants cows in
    cowOrder = [int(item) for item in list1]
    vetOrder = [int(item) for item in list2]
totalCowChecked = 0
        
def reorder(order, l, r):
    order[l], order[r] = order[r], order[l]
    return order

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        reorder(cowOrder, i, j)
        count = 0
        if cowOrder[i] == vetOrder[i]:
            totalCowChecked += 1
            count += 1
            print(cowOrder, vetOrder, cowOrder[i], cowOrder[j])
print(totalCowChecked)

