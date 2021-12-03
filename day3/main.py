def main():
    with open('input.txt') as f:
        res = [i.rstrip() for i in f.readlines()]

    # 3.1
    ones = {}
    for num in res:
        for idx, letter in enumerate(num):
            if idx not in ones:
                ones[idx] = 0
            if letter == '1':
                ones[idx] += 1

    gamma = "".join(
        '1' if value > len(res) // 2 else '0' for _, value in ones.items()
    )
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    print(int(gamma,2)*int(epsilon,2))


    #3.2
    oxygen = res.copy()
    co2 = res.copy()

    idx = 0
    while len(oxygen) > 1:
        ones = [i for i in oxygen if i[idx] == '1']
        zeros = [i for i in oxygen if i[idx] == '0']
        oxygen = ones if len(ones) >= len(zeros) else zeros
        idx += 1

    idx = 0
    while len(co2) > 1:
        ones = [i for i in co2 if i[idx] == '1']
        zeros = [i for i in co2 if i[idx] == '0']
        co2 = zeros if len(zeros) <= len(ones) else ones
        idx += 1

    print(int(oxygen[0],2)*int(co2[0],2))


if __name__ == '__main__':
    main()