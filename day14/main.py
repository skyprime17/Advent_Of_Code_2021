from collections import defaultdict, Counter
from itertools import zip_longest, pairwise

with open('input.txt') as f:
    result = [i.strip() for i in f.readlines()]


def main():
    #14.1
    insertion_rules = defaultdict(str)
    template = result[0]
    for p in result[2:]:
        px, py = p.split(" -> ")
        insertion_rules[px] = py

    for _ in range(10):
        xs = list(pairwise(template))
        ys = [insertion_rules[x + y] for (x, y) in xs if x + y in insertion_rules]
        xx = list(zip_longest(template, ys, fillvalue=''))
        template = ''.join(map(lambda x: x[0] + x[1], xx))
    c = Counter(template)
    print(c.most_common()[0][1] - c.most_common()[-1][1])


if __name__ == '__main__':
    main()
