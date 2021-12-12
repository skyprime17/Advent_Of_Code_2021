from collections import defaultdict
from time import perf_counter
with open('input.txt') as f:
    result = [i.strip() for i in f.readlines()]

#12.1
def find_path_to_end(pos, visited, xs, end):
    if pos == 'end':
        end.append(visited)
        return
    for p in xs[pos]:
        if p in visited and p.islower():
            continue
        cached_path = visited.copy()
        cached_path.append(p)
        find_path_to_end(p, cached_path, xs, end)


#12.2
def find_path_to_end2(pos, visited, xs, end):
    if pos == 'end':
        end.append(visited)
        return

    lowercase_list = [i for i in visited if i.islower()]
    # check if i already have 2 lowercase caves in visited
    if len(lowercase_list) - len(set(lowercase_list)) == 2:
        return

    for p in xs[pos]:
        if p == 'start':
            continue
        cached_path = visited.copy()
        cached_path.append(p)
        find_path_to_end2(p, cached_path, xs, end)


def main():
    xs = defaultdict(list)
    for line in result:
        x, j = line.split("-")
        xs[x].append(j)
        xs[j].append(x)

    visited = ["start"]
    #12.1
    end_ = []
    find_path_to_end("start", visited, xs, end_)
    print("Part 1", len(end_))
    
    #12.2
    end_ = []
    find_path_to_end2("start", visited, xs, end_)
    print("Part 2", len(end_))


if __name__ == '__main__':
    main()
