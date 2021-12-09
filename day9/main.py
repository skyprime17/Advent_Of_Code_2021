from functools import reduce

with open('input.txt') as f:
    result = [[int(i) for i in x.rstrip()] for x in f.readlines()]


def rec(dirs, i, j, visited):
    if i < 0 or j < 0 or i > len(result) - 1 or j > len(result[0]) - 1 or result[i][j] == 9:
        return
    visited.add((i, j))
    next_moves = []
    for (dx, dy) in dirs:
        ni = dx + i
        nj = dy + j
        next_moves.append((ni, nj))
    [rec(dirs, x, j, visited)
     for (x, j) in next_moves if (x, j) not in visited]


def main():
    # 9.1
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    c = 0
    for i in range(len(result)):
        for j in range(len(result[i])):
            vals = []
            for (dx, dy) in dirs:
                ni = dx + i
                nj = dy + j
                if ni < 0 or nj < 0 or ni > len(result) - 1 or nj > len(result[0]) - 1:
                    continue
                else:
                    vals.append(result[ni][nj])
            if result[i][j] < min(vals):
                c += result[i][j] + 1
    print("Result for part 1 =", c)

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    size = []
    for i in range(len(result)):
        for j in range(len(result[i])):
            vals = []
            for (dx, dy) in dirs:
                ni = dx + i
                nj = dy + j
                if ni < 0 or nj < 0 or ni > len(result) - 1 or nj > len(result[0]) - 1:
                    continue
                else:
                    vals.append(result[ni][nj])
            if result[i][j] < min(vals):
                visited = set()
                rec(dirs, i, j, visited)
                size.append(len(visited))
                # print(result[i][j])

    lava_thingy = reduce(lambda x, y: x * y, sorted(size)[-3:])
    print("Result for part 2 =", lava_thingy)


if __name__ == '__main__':
    main()
