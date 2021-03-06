import time

# move class
class Move():
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return "({} {})".format(self.r, self.c)


# board class
class Board():
    def __init__(self):
        self.layout = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self._complete = False

    def __str__(self):
        r1 = " ".join(self.layout[0])
        r2 = " ".join(self.layout[1])
        r3 = " ".join(self.layout[2])
        return "------\n{}\n{}\n{}\n------".format(r1, r2, r3)
    
    def make_move(self, m, p):
        r = m.r
        c = m.c
        self.layout[r][c] = p

    def undo_move(self, m):
        r = m.r
        c = m.c
        self.layout[r][c] = "_"
    
    def moves_left(self):
        for r in self.layout:
            for c in r:
                if c == "_":
                    return True
        return False
    
    def get_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.layout[i][j] == "_":
                    moves.append(Move(r=i, c=j))
        return moves

    def end_game(self):
        self._complete = True

    def is_complete(self):
        return self._complete

# evaluate function to tell final score
def evaluate(b):
    # check if any completed rows
    for r in b.layout:
        if r[0] == r[1] and r[1] == r[2]:
            if r[0] == "X":
                return 1
            elif r[0] == "O":
                return -1

    # check if any completed columns
    for i in range(len(b.layout)):
        if b.layout[0][i] == b.layout[1][i] and b.layout[1][i] == b.layout[2][i]:
            if b.layout[0][i] == "X":
                return 1
            elif b.layout[0][i] == "O":
                return -1
    
    # checking for diagonals
    if b.layout[0][0] == b.layout[1][1] and b.layout[1][1] == b.layout[2][2]:
        if b.layout[0][0] == "X":
            return 1
        elif b.layout[0][0] == "O":
            return -1

    if b.layout[0][2] == b.layout[1][1] and b.layout[1][1] == b.layout[2][0]:
        if b.layout[0][2] == "X":
            return 1
        elif b.layout[0][2] == "O":
            return -1
    
    # else return 0 for tie
    return 0



# minimax function
def minimax(b, p):
    if not b.moves_left():
        return evaluate(b)

    if p == "X":
        v = float("-inf")
        for move in b.get_moves():
            b.make_move(move, p)
            v = max(v, minimax(b, "O"))
            b.undo_move(move)
    elif p == "O":
        v = float("inf")
        for move in b.get_moves():
            b.make_move(move, p)
            v = min(v, minimax(b, "X"))
            b.undo_move(move)
    return v


def get_best_move(b, p):
    best_move = Move(r=-1, c=-1)
    if p == "X":
        best_v = float("-inf")
        for move in b.get_moves():
            b.make_move(move, p)
            v = max(best_v, minimax(b, "O"))
            b.undo_move(move)
            if (v > best_v):
                best_move.r = move.r
                best_move.c = move.c
                best_v = v
    elif p == "O":
        best_v = float("inf")
        for move in b.get_moves():
            b.make_move(move, p)
            v = min(best_v, minimax(b, "X"))
            b.undo_move(move)
            if (v < best_v):
                best_move.r = move.r
                best_move.c = move.c
                best_v = v
    return best_move


b = Board()
opponent = False

while b.moves_left() and not b.is_complete():
    p = "X" if not opponent else "O"
    move = get_best_move(b, p)
    b.make_move(move, p)
    print(b)
    opponent = not opponent
    if evaluate(b) != 0:
        b.end_game()
    time.sleep(1)
        