def main():
    with open('input.txt', 'r') as f:
        res = [int(i) for i in f.readlines()]

    #   1.1
    inc1 = sum(
        res[idx] < res[idx + 1] for idx, i in enumerate(res[:-1])
    )
    print(inc1)

    #   1.2
    inc = sum(
        sum(res[idx: idx + 3:]) < sum(res[idx + 1: idx + 4])
        for idx, i in enumerate(res)
    )
    print(inc)


if __name__ == '__main__':
    main()
