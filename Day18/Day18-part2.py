from utils.api import get_input

inp = get_input(18)
pos = [0, 0]
points = []
border = 0
for line in inp.splitlines():
    colour = line.split()[-1][2:]
    amount = int(colour[:5], 16)
    direction = int(colour[5])
    match direction:
        case 3:
            pos[1] -= amount
        case 0:
            pos[0] += amount
        case 1:
            pos[1] += amount
        case 2:
            pos[0] -= amount
    border += abs(amount)
    points.append(pos.copy())

# shoelace formula from here: https://stackoverflow.com/a/19875560/13683643 :(
print(
    int(
        abs(
            sum(
                points[i][0] * (points[i + 1][1] - points[i - 1][1])
                for i in range(-1, len(points) - 1)
            )
        )
        / 2.0
        + border / 2
        + 1
    )
)