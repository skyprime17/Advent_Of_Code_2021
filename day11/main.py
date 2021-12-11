import os
from time import sleep
from colorama import init
from colorama import Fore, Back, Style


init()

with open('input.txt') as f:
    result = [[int(i) for i in x.rstrip()] for x in f.readlines()]

def rec(dirs, i, j):
    if i < 0 or j < 0 or i > len(result) - 1 or j > len(result[0]) - 1 or result[i][j] == 10:
        return
    result[i][j] += 1
    next_moves = []
    if result[i][j] == 10:
        for (dx, dy) in dirs:
            ni = dx + i
            nj = dy + j
            next_moves.append((ni, nj))

    [rec(dirs, x, j) for (x, j) in next_moves]


def main():
    # 11.1
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    c = 0
    for _ in range(100):
        for i in range(len(result)):
            for j in range(len(result[i])):
                rec(dirs, i, j)
        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][j] > 9:
                    result[i][j] = 0
                    c+=1

    print(result)
    print(c)

def main2():
    # 11.2
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (1, 1), (-1, 1), (1, -1)]
    steps = 0
    flashes = 0
    while True:
        os.system('cls')
        print(Fore.WHITE+f"Steps: {steps}")
        print(Fore.WHITE+f"Flashes: {flashes}")
        for line in result:
            for num in line:
                if num == 0:
                    print(Fore.WHITE + str(num), end=" ",flush=True)
                else:
                    print(Fore.RED + str(num), end=" ", flush=True)
            print(flush=True)
        print(flush=True)
        sleep(.1)
        if sum(map(sum,result)) == 0:
            break
        for i in range(len(result)):
            for j in range(len(result[i])):
                rec(dirs, i, j)
                            
        for i in range(len(result)):
            for j in range(len(result[i])):
                if result[i][j] > 9:
                    result[i][j] = 0
                    flashes +=1
        steps +=1


if __name__ == '__main__':
    #main()
    main2()
