def main():
    with open('input.txt', 'r') as f:
        res = [i for i in f.readlines()]

    # 2 .1
    instr = {
        "up": 0,
        "down": 0,
        "forward": 0
    }

    for i in res:
        xs = i.split()
        instr[xs[0]] += int(xs[-1])

    print(instr.get('forward') * abs(instr.get('up') - instr.get('down')))

    # 2.2
    depth = 0
    horizontal = 0
    aim = 0

    for i in res:
        xs = i.split()
        if xs[0] == 'down':
            aim += int(xs[-1])
        elif xs[0] == 'up':
            aim -= int(xs[-1])
        else:
            horizontal += int(xs[-1])
            if aim != 0:
                depth += int(xs[-1]) * aim
    print(horizontal * depth)



if __name__ == '__main__':
    main()
