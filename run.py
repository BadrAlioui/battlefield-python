import random
from colorama import Fore, init

# Initialize color output
init(autoreset=True)

BANNER = '''
 #####    ##   ##### ##### #      ######  ####  #    # # #####   ####     
 #    #  #  #    #     #   #      #      #      #    # # #    # #         
 #####  #    #   #     #   #      #####   ####  ###### # #    #  ####     
 #    # ######   #     #   #      #           # #    # # #####       #    
 #    # #    #   #     #   #      #      #    # #    # # #      #    #    
 #####  #    #   #     #   ###### ######  ####  #    # # #       ####      
'''

def drawfield(field):
    """
    Draws the game board using the provided 2D list.
    """
    for row in field:
        for cell in row:
            if cell == '@':
                print(Fore.GREEN + cell, end=' ')
            elif cell == 'X':
                print(Fore.RED + cell, end=' ')
            elif cell == '-':
                print(Fore.WHITE + cell, end=' ')
            elif cell == '£':
                print(Fore.BLUE + cell, end=' ')
            elif cell == '$':
                print(Fore.YELLOW + cell, end=' ')
            else:
                print(Fore.CYAN + cell, end=' ')
        print()
    print()


def random_number(board, symbol):
    """
    Place 4 ships randomly on the board using the given symbol.
    """
    positions = set()
    while len(positions) < 4:
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if (row, col) not in positions:
            positions.add((row, col))
            board[row][col] = symbol


def get_valid_name():
    """
    Prompt the user for a name containing only letters.
    """
    while True:
        name = input(Fore.GREEN + 'Enter your name: ')
        if name.isalpha():
            return name
        print(Fore.RED + 'Name must contain only letters. Please try again.')


def get_valid_guess(already_guessed):
    """
    Prompt for a row and column guess, ensure integers 0-4 and not guessed before.
    """
    while True:
        try:
            row = int(input('Guess a row (0-4): '))
            col = int(input('Guess a column (0-4): '))
            if not (0 <= row <= 4 and 0 <= col <= 4):
                raise ValueError
            if (row, col) in already_guessed:
                print(Fore.RED + 'You\'ve already guessed that location. Choose another.')
                continue
            return row, col
        except ValueError:
            print(Fore.RED + 'Invalid input. Enter numbers between 0 and 4.')


def main():
    print('*' * 75)
    print(BANNER)
    print('Welcome to Ultimate BATTLESHIPS!')
    print('Board size: 5x5, Ships per side: 4, Turns: 5')
    print('*' * 75)

    name = get_valid_name()
    player_score = 0
    computer_score = 0

    # Initialize boards
    player_board = [['-' for _ in range(5)] for _ in range(5)]
    computer_board = [['-' for _ in range(5)] for _ in range(5)]
    display_board = [['-' for _ in range(5)] for _ in range(5)]

    # Place ships
    random_number(player_board, '@')
    random_number(computer_board, "'")

    print(f"\n{name}'s Board:")
    drawfield(player_board)
    print("Computer's Board:")
    drawfield(display_board)

    guessed = set()
    turns = 0
    while turns < 5 and player_score < 4 and computer_score < 4:
        # Player's turn
        row, col = get_valid_guess(guessed)
        guessed.add((row, col))
        turns += 1

        if computer_board[row][col] == "'":
            print(Fore.YELLOW + 'Hit! You sank an enemy ship!')
            display_board[row][col] = '$'
            player_score += 1
        else:
            print(Fore.RED + 'Miss!')
            display_board[row][col] = 'X'

        drawfield(display_board)

        # Computer's turn
        comp_row, comp_col = get_valid_guess(guessed)
        guessed.add((comp_row, comp_col))
        print(f"Computer guesses: ({comp_row}, {comp_col})")
        if player_board[comp_row][comp_col] == '@':
            print(Fore.BLUE + 'Computer hit your ship!')
            player_board[comp_row][comp_col] = '£'
            computer_score += 1
        else:
            print(Fore.WHITE + 'Computer missed.')

        drawfield(player_board)
        print(Fore.CYAN + f"Score -> {name}: {player_score} | Computer: {computer_score}")
        print('-' * 50)

    # Game result
    if player_score > computer_score:
        print(Fore.GREEN + f"Congratulations {name}, you won!")
    elif player_score < computer_score:
        print(Fore.RED + f"Sorry {name}, you lost.")
    else:
        print(Fore.YELLOW + "It's a draw!")

    # Ask to play again
    while True:
            play_again = input('Would you like to play another game? (y/n)\n').lower()
            if play_again in ('y', 'n'):
                break
            print(Fore.RED + "Please enter 'y' or 'n'.")

    print(Fore.CYAN + 'Thanks for playing!')

if __name__ == '__main__':
    main()

