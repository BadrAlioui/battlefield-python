import random
from colorama import Fore, init

init(autoreset=True)

BOARD_SIZE = 5
SHIPS_COUNT = 4

def init_board():
    return [['-' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def place_ships(board, symbol):
    positions = set()
    while len(positions) < SHIPS_COUNT:
        r, c = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
        if (r, c) not in positions:
            positions.add((r, c))
            board[r][c] = symbol


