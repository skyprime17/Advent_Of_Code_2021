with open('input.txt') as f:
    res = [int(i) for i in f.read().strip().split(",")]


def main():

    #   6.1
    # for day in range(80):
    #    for idx,j in enumerate(res):
    #        res[idx] = j-1
    #        if j == 0:
    #            res[idx] = 6
    #            res.append(9)
    # print(days)

    #   6.2 
    index = {i: 0 for i in range(9)}
    for i in res:
        index[i] += 1

    for i in range(256):
        temp = {i: 0 for i in range(9)}
        for k, v in index.items():
            if k == 0:
                temp[8] += v
                temp[6] += v
            else:
                temp[k-1] += v
        index = temp

    print(sum(index.values()))

if __name__ == '__main__':
    main()
