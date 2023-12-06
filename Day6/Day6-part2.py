def solve(data):

    times = int(''.join([t for t in data[0].split(':')[-1].split()]))
    records = int(''.join([t for t in data[1].split(':')[-1].split()]))

    t = times
    target = records
    wins = 0

    for h in range( t +1):
        dist = h * ( t -h)
        if dist > target:
            wins += 1

    solution = wins

    return solution


def main():
    input="""Time:        41     66     72     66
Distance:   244   1047   1228   1040"""
    input_ = input.splitlines()
    # with open('input') as in_f:
    #     for row in in_f:
    #         v = row.strip()
    #         input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()