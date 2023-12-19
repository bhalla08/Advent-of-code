from heapq import heappop, heappush

from utils.api import get_input

inp = get_input(17)
grid = []
for line in inp.splitlines():
    l = []
    for char in line:
        l.append([int(char), {}])
    grid.append(l)

end = [len(grid[0]) - 1, len(grid) - 1]
queue = []
visited = set()

heappush(queue, (0, 1, [0, 0], 0, 1))
heappush(queue, (0, 2, [0, 0], 0, 2))

while queue:
    total, direction, pos, streak, previous_direction = heappop(queue)
    d = (direction, tuple(pos), streak, previous_direction)
    if d in visited:
        continue
    visited.add(d)
    if direction == previous_direction:
        streak += 1
    else:
        streak = 0
    if streak >= 3:
        continue
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
        continue
    try:
        tile = grid[pos[1]][pos[0]]
    except IndexError:
        continue
    total += tile[0]
    if pos == end:
        print(total)
        break
    opposite_direction = (direction - 2) % 4
    for x in range(4):
        if x == opposite_direction:
            continue
        heappush(queue, (total, x, pos, streak, direction))