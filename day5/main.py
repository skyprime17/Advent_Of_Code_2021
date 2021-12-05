import re

with open('input.txt') as f:
    res = [i.rstrip() for i in f.readlines()]

def main():
    res2 = [re.findall('\d+', i) for i in res]
    index = {}
    for c in res2:
        x1 = int(c[0])
        x2 = int(c[2])
        y1 = int(c[1])
        y2 = int(c[3])

        dx = 1 if x2 > x1 else 0 if x2 == x1 else -1
        dy = 1 if y2 > y1 else 0 if y2 == y1 else -1

        while True:
            if(x1==x2+dx) and (y1==y2+dy):
                break
            if(x1, y1) in index:
                index[(x1, y1)] += 1
            else:
                index[(x1, y1)] = 0
            x1 += dx
            y1 += dy
    s = sum(value > 0 for _, value in index.items())
    print(s)


if __name__ == '__main__':
    main()
