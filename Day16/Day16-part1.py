from sys import setrecursionlimit

from utils.api import get_input

inp = get_input(16)
setrecursionlimit(10000)
grid = []
for line in inp.splitlines():
    l = []
    for char in line:
        l.append([char, []])
    grid.append(l)


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


go(1, [-1, 0])
count = 0
for y in grid:
    for x in y:
        if x[1]:
            count += 1
            print("#", end="")
        else:
            print(".", end="")
    print()
print(count)