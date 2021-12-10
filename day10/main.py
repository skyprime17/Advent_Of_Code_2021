with open('input.txt') as f:
    result = [[i for i in x.rstrip()] for x in f.readlines()]

chars_map = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<"
    }


score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


chars_map2 = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}


scores2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def check(arr):
    stack = []
    for i in arr:
        if i in chars_map.values():
            stack.append(i)
            continue
        if chars_map[i] == stack[-1]:
            stack.pop()
        else:
            return i
    return stack

def check2(arr):
    xs = check(arr)
    if len(xs) == 1:
        return None
    xs_completed = [chars_map2[i] for i in xs[::-1]]
    s = 0
    for i in xs_completed:
        s *= 5
        s += scores2[i]
    return s 


def main():
    #10.1
    s = 0
    for i in result:
        r = check(i)
        s+= score[r] if len(r) == 1 else 0
    print(s)
    
    #10.2
    results = [check2(i) for i in result if check2(i) is not None]
    print(sorted(results)[len(results)//2])

if __name__ == '__main__':
    main()
