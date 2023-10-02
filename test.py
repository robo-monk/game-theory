# If there's only one coin left, it's a P-position.
# If there's a move that leads to a P-position, then the current position is an N-position.
# If all moves lead to N-positions, then the current position is a P-position.

NUM_OF_COINS = 21
MAX_COINS_PER_TURN = 3
MISERE = False

def find_legal_moves(coins: int):
    return [i for i in range(1, min(coins, MAX_COINS_PER_TURN) + 1)]


def is_game_over(coins: int):
    return coins == 0

def get_winning_player(coins: int, analysis: list[str]):
    if coins == 0:
        return 'N' if MISERE else 'P'
    
    for move in find_legal_moves(coins):
        next_position = coins - move
        if analysis[next_position] == 'P':
            return 'N'

    return 'P'


analysis: list[str] = []
for position in range(0, NUM_OF_COINS):
    winning_player = get_winning_player(position, analysis)
    analysis.append(winning_player)


print("Position | Result")
print("-----------------")
for idx, result in enumerate(analysis):
    print(f"{idx:8} | {result}")
