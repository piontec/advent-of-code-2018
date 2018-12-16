grid_size = 300

def cell_value(x, y, serial_num):
    rid = x + 10
    n = (rid * y + serial_num) * rid
    return int((n % 1000) / 100) - 5


def square_value(x, y, size, cells):
    return sum (cells[a, b] for a in range(x, x + size) for b in range(y, y + size))


def get_cells(serial_num):
    return {(x, y): cell_value(x, y, serial_num) for y in range(1, grid_size+1) for x in range(1, grid_size+1)}


def get_max_cell(size, cells):    
    squares = {(x, y): square_value(x, y, size, cells) for y in range(1, grid_size+2-size) 
        for x in range(1, grid_size+2-size)}
    max_coords = max(squares, key=lambda s: squares[s])
    return max_coords, squares[max_coords]


def square_value_with_prev(x, y, size, cells, prev):
    return prev[(x, y)] + sum([cells[(size, y)] for y in range(1, size+1)]) + sum([cells[x, size] 
        for x in range(1, size)])
    

def get_max_cell_with_prev(size, cells, prev):
    print("Running for size {}".format(size))    
    squares = {(x, y): square_value_with_prev(x, y, size, cells, prev) for y in range(1, grid_size+2-size) 
        for x in range(1, grid_size+2-size)}    
    return squares

# test case - expected 29 with (33,45)
c = get_cells(18)
prev = c
for i in range(2, 4):
    prev = get_max_cell_with_prev(i, c, prev)
max_coords = max(prev, key=lambda s: prev[s])
max_val = prev[max_coords]
assert max_val == 29
assert max_coords == (33, 45)

# prev = c
# for i in range(2, 4):
#     max_coords, prev = get_max_cell_with_prev(i, c, prev)
#     print((max_coords, prev[max_coords]))


# c = get_cells(9110)
# # part1
# print(get_max_cell(3, c))

# prev = c
# for i in range(2, 4):
#     max_coords, prev = get_max_cell_with_prev(i, c, prev)
#     print((max_coords, prev[max_coords]))

# # part2
# # per_size = [get_max_cell(s, c) for s in range(1, 300)]
# # max_size = max(per_size, key=lambda e: per_size[e][1])
# # print("Best size: {} with {}", max_size+1, per_size[max_size])