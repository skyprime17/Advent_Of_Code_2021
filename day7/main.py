with open('input.txt') as f:
    res = [int(i) for i in f.read().strip().split(",")]


def main():
    # 7.1
    fuel = [sum(map(lambda x: abs(x-i), res)) for i in range(min(res), max(res))]
    print(min(fuel))

    #7.2
    fuel2 = [sum(map(lambda x: (abs(x-i)*(abs(x-i)+1))//2, res)) for i in range(min(res), max(res))]
    print(min(fuel2))

if __name__ == '__main__':
    main()
