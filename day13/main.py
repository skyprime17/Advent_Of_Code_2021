from collections import defaultdict

with open('input.txt') as f:
    result = [i.strip() for i in f.readlines()]


def main():
    #13.1
    dots = []
    instructions = []
    for line in result:
        if not line:
            continue
        elif line.startswith('fold'):
            x,y = line.replace('fold along ', '').split('=')
            instructions.append((x,int(y)))
            continue
        x,y = line.split(',')
        dots.append((int(x),int(y)))

    for idx, (instr, dot) in enumerate(instructions):
        print(idx, len(set(dots)))
        if instr == 'y':
            y_fold = dot
            for idx, (x,y) in enumerate(dots):
                #example: fold along y_fold=7 and y=10
                #if y > y_fold then y = y_fold -abs(y-y_fold)
                #True -> y =7-(3) -> y=4
                if y > y_fold:
                    new_y = y_fold - abs(y- y_fold)
                    dots[idx] = (x,new_y)
        elif instr == 'x':
            x_fold = dot
            for idx, (x, y) in enumerate(dots):
                if x > x_fold:
                    new_x = x_fold - abs(x - x_fold)
                    dots[idx] = (new_x, y)

    #13.2
    xs = list(set(dots))
    x_max = max(xs, key=lambda i:i[0])[0]+1
    y_max = max(xs, key=lambda i:i[1])[1]+1
    ys = [[' ']*x_max for _ in range(y_max)]
    for (x,y) in xs:
        ys[y][x] = '#'
    for line in ys:
        print("".join(line))

    
if __name__ == '__main__':
    main()
