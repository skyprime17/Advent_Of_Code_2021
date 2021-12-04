from dataclasses import dataclass, field
from typing import List

with open('input.txt') as f:
    res:List[str] = [i.rstrip() for i in f.readlines()]


@dataclass
class BingoBoard:
    board:List[List[int]]
    board_draws: List[List[bool]] = field(default=False, init=False)
    needed_turns: int = field(default=None, init=False)
    draws: List[int] = field(default_factory=list,init=False)
    last_num:int = field(default=None)
    score:int = field(default=0)
    done:bool = field(default=False)


    def __post_init__(self):
        self.board_draws = [[False for _ in range(5)] for _ in range(5)]

    def check_winner(self):
        for i in range(len(self.board_draws)):
            if all(self.board_draws[i]) or all(self.board_draws[j][i] for j in range(len(self.board_draws))):
                self.needed_turns = len(self.draws)
                self.done = True
                return True
        self.done = False
        return False

    def add_draw(self, num):
        self.last_num = num
        self.draws.append(num)

    def do_move(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] in self.draws:
                    self.board_draws[i][j] = True

    def calc_score(self):
        s = 0
        for i in range(len(self.board_draws)):
            for j in range(len(self.board_draws)):
                if not self.board_draws[i][j]:
                    s += self.board[i][j]
        self.score =  s * self.last_num

def main():
    draws:int = [int(i) for i in res[0].split(',')]
    boards:List[BingoBoard] = []
    board:int = []

    for line in res[2:]:
        if line:
            board.append([int(j) for j in line.split()])
        else:
            boards.append(BingoBoard(board))
            board = []

    scores:List[int] = []

    for i in draws:
        for j in boards:
            if j.done:
                continue
            j.add_draw(i)
            j.do_move()
            if j.check_winner():
                j.calc_score()
                scores.append(j.score)

    print(scores[0])    #first score is the one with the least turns
    print(scores[-1])   #last score is the one with the most turns

if __name__ == '__main__':
    main()
