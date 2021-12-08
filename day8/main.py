with open('input.txt') as f:
    res = [i.strip() for i in f.readlines()]


def main():
    #8.1
    c = 0
    for line in res:
        signals = line.split(' | ')[1].split(' ')
        c += len(list(filter(lambda x: len(x) in [2, 4, 3, 7], signals)))
    print(c)

    #8.2
    result = 0
    for line in res:
        signals = [''.join(sorted(i)) for i in line.split(' | ')[0].split(' ')]
        output = [i for i in line.split(' | ')[1].split(' ')]

        xs = {i:None for i in range(10)}
        for i in signals:
            if len(i) == 2:
                xs[1] = i
            elif len(i) == 3:
                xs[7] = i
            elif len(i) == 4:
                xs[4] = i
            elif len(i) == 7:
                xs[8] = i
        for i in signals:
            if len(i) == 5:
                if len(set(xs[1]).intersection(i)) == 2:
                    xs[3] = i
                elif len(set(xs[4]).intersection(i)) == 2:
                    xs[2] = i
                else:
                    xs[5] = i
        for i in signals:
            if len(i) == 6:
                if len(set(xs[3]).intersection(i)) == 5:
                    xs[9] = i
                elif len(set(xs[5]).intersection(i)) == 5:
                    xs[6] = i
                else:
                    xs[0] = i
        s = ""
        for i in output:
            for k,v in xs.items():
                if set(i) == set(v):
                    s += str(k)
        result += int(s)
    print(result)
        
if __name__ == '__main__':
    main()
