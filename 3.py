from libs import ulamspiral

n = 361527

spiral = ulamspiral.UlamSpiral(n)

index_1_x = 0
index_1_y = 0
index_n_x = 0
index_n_y = 0

for i, row in enumerate(spiral.rows):
    if 1 in row:
        index_1_x = row.index(1)
        index_1_y = i
    if n in row:
        index_n_x = row.index(n)
        index_n_y = i


def distance(index_1_x, index_1_y, index_n_x, index_n_y):
    return abs(index_1_x - index_n_x) + abs(index_1_y - index_n_y)


print(distance(index_1_x, index_1_y, index_n_x, index_n_y))
