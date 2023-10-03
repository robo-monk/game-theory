# If there's only one coin left, it's a P-position.
# If there's a move that leads to a P-position, then the current position is an N-position.
# If all moves lead to N-positions, then the current position is a P-position.

from functools import lru_cache


PILE_SIZE = 31
SUBSTRACTION_SET = [ 1, 3, 4 ]
MISERE = False

N = 'N'
P = 'P'

def find_legal_moves(pile: int):
    return [i for i in SUBSTRACTION_SET if i <= pile]


def is_game_over(pile: int):
    return pile == 0

def get_winning_player(pile: int, analysis: list[str]):
    if pile == 0:
        return N if MISERE else P 
    
    for move in find_legal_moves(pile):
        next_position = pile - move
        if analysis[next_position] == P:
            return N 

    return P 

def mex(_set: list):
    _mex = 0
    while _mex in _set:
        _mex += 1

    return _mex

@lru_cache
def sprague_grundy(pile: int):
    moves = find_legal_moves(pile)
    # print("sg", pile, moves)
    if len(moves) == 0:
        return 0
    else:
        move_indeces = [
            pile - m for m in moves
        ]
        # print("-> ", move_indeces)
        v_set = [
            sprague_grundy(m) for m in move_indeces
        ]
        # print("MEX->", mex(v_set), v_set)
        return mex(v_set)


analysis: list[str] = []
for position in range(0, PILE_SIZE+1):
    winning_player = get_winning_player(position, analysis)
    analysis.append(winning_player)


print("Position | Result | SG")
print("-----------------")
for idx, result in enumerate(analysis):
    sg = sprague_grundy(idx)
    print(f"{idx:8} | {result:4} | {sg:5}")
    # if (idx > 1): break
