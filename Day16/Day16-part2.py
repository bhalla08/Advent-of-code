from copy import deepcopy
from sys import setrecursionlimit

from utils.api import get_input

inp = get_input(16)
setrecursionlimit(10000)
original_grid = []
for line in inp.splitlines():
    l = []
    for char in line:
        l.append([char, []])
    original_grid.append(l)


def go(direction, pos):
    pos = pos.copy()
    match direction:
        case 0:
            pos[1] -= 1
        case 1:
            pos[0] += 1
        case 2:
            pos[1] += 1
        case 3:
            pos[0] -= 1
    if pos[0] < 0 or pos[1] < 0:
        return
    try:
        tile = grid[pos[1]][pos[0]]
    except IndexError:
        return
    if direction in tile[1]:
        return
    tile[1].append(direction)
    match tile[0]:
        case ".":
            go(direction, pos)
        case "|":
            match direction:
                case 0 | 2:
                    go(direction, pos)
                case 1 | 3:
                    go(0, pos)
                    go(2, pos)
        case "-":
            match direction:
                case 1 | 3:
                    go(direction, pos)
                case 0 | 2:
                    go(1, pos)
                    go(3, pos)
        case "/":
            match direction:
                case 0:
                    go(1, pos)
                case 1:
                    go(0, pos)
                case 2:
                    go(3, pos)
                case 3:
                    go(2, pos)
        case "\\":
            match direction:
                case 0:
                    go(3, pos)
                case 1:
                    go(2, pos)
                case 2:
                    go(1, pos)
                case 3:
                    go(0, pos)


def count_energized(grid_):
    count = 0
    for y in grid_:
        for x in y:
            if x[1]:
                count += 1
    return count


high = 0
for x in range(len(original_grid[0])):
    grid = deepcopy(original_grid)
    go(2, [x, -1])
    c = count_energized(grid)
    if c > high:
        high = c
for x in range(len(original_grid[0])):
    grid = deepcopy(original_grid)
    go(0, [x, len(original_grid)])
    c = count_energized(grid)
    if c > high:
        high = c
for y in range(len(original_grid)):
    grid = deepcopy(original_grid)
    go(1, [-1, y])
    c = count_energized(grid)
    if c > high:
        high = c
for y in range(len(original_grid)):
    grid = deepcopy(original_grid)
    go(3, [len(original_grid[0]), y])
    c = count_energized(grid)
    if c > high:
        high = c
print(high)