matrix = []
target = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)
    if 1 in row:
        target = [i, row.index(1)]
moves = abs(target[0] - 2) + abs(target[1] - 2)
print(moves)
   