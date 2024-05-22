import random
from colorama import Fore, init

init(autoreset=True)

BANNER = ''' 
'########:::::'###::::'########:'########:'##:::::::'########::'######::'##::::'##:'####:'########:::'######::::
 ##.... ##:::'## ##:::... ##..::... ##..:: ##::::::: ##.....::'##... ##: ##:::: ##:. ##:: ##.... ##:'##... ##:::
 ##:::: ##::'##:. ##::::: ##::::::: ##:::: ##::::::: ##::::::: ##:::..:: ##:::: ##:: ##:: ##:::: ##: ##:::..::::
 ########::'##:::. ##:::: ##::::::: ##:::: ##::::::: ######:::. ######:: #########:: ##:: ########::. ######::::
 ##.... ##: #########:::: ##::::::: ##:::: ##::::::: ##...:::::..... ##: ##.... ##:: ##:: ##.....::::..... ##:::
 ##:::: ##: ##.... ##:::: ##::::::: ##:::: ##::::::: ##:::::::'##::: ##: ##:::: ##:: ##:: ##::::::::'##::: ##:::
 ########:: ##:::: ##:::: ##::::::: ##:::: ########: ########:. ######:: ##:::: ##:'####: ##::::::::. ######::::
........:::..:::::..:::::..::::::::..:::::........::........:::......:::..:::::..::....::..::::::::::......:::::
'''

# Function to draw the game board
def drawfield(field):
  '''
  Draws the game board using the provided array.
  '''
  for row in range(5):
    for col in range(10):
      if col % 2 == 0:
        rightColumn = col // 2
        cell = field[row][rightColumn]
        if cell == "@":
          print(Fore.GREEN + cell, end="")
        elif cell == "X":
          print(Fore.RED + cell, end="")
        elif cell == '-':
          print(Fore.WHITE + cell, end="")
        elif cell == "£":
          print(Fore.BLUE + cell, end="")
        elif cell == "$":
          print(Fore.YELLOW + cell, end="")
        else:
          print(Fore.CYAN + cell, end="")
      else:
        print(" ", end="")
    print(' ')


anotherGame = True
while anotherGame:

  # Display the game initialization message
  print('**********************************')
  print(BANNER)
  print(
    "Welcome to Ultimate BATTLESHIPS! !\nBoard size: 5. Number of ships : 4\nTop left corner is row: 0, col: 0'\nAnd you have 5 turns to sink all the ships\nGood Luck!"
  )
  print('**********************************')

  # Prompt the user to enter their name
  while True:
    name = input(Fore.GREEN + "Enter your Name:\n")
    if not name.isalpha():
      print(Fore.RED + "Enter only name with letters, please.")
    else:
      break
  # Initialize the scores dictionary
  scores = {"computer": 0, "player": 0}

  # Create arrays to represent the player and computer boards
  currentPlayer = [list(('-') * 5) for i in range(5)]
  currentComputer = [list(('-') * 5) for i in range(5)]
  fieldCommun = [list(('-') * 5) for i in range(5)]

  # Function to generate random numbers for ship positions
  def random_number(gamer):
    '''
    Generates random positions for ships on the board.
    Takes the board array (either player or computer) as an argument to place the ships.
    '''
    liste_set = set()
    while len(liste_set) < 4:
      row = random.randint(0, 4)
      col = random.randint(0, 4)
      movecompRow = row
      movecompColumn = col
      if row not in liste_set and col not in liste_set:

        liste_set.add((movecompRow, movecompColumn))
        if gamer == currentPlayer:
          currentPlayer[movecompRow][movecompColumn] = "@"
        else:
          currentComputer[movecompRow][movecompColumn] = "'"

  # Populate the boards with ships
  random_number(currentPlayer)
  random_number(currentComputer)

  # Display the player's board
  print()
  print(f"{name}'s Board")
  print()
  drawfield(currentPlayer)

  print()
  print('----------------------------------')
  print()
  print('Computer\'s Board: ')
  print()

  # Display the computer's board with ships hidden
  drawfield(fieldCommun)

  # Game play loop
  print()
  playAgain = 'y'
  tries = 0
  while playAgain == 'y' and tries < 5:

    while True:

      try:

        moveRow = int(input("Guess a row between 0 and 4: \n"))
        moveColumn = int(input("Guess a column between 0 and 4: \n"))

        if moveRow < 0 or moveRow > 4 or moveColumn < 0 or moveColumn > 4:
          raise ValueError(
            Fore.RED + 'Invalid input. Please enter a number between 0 and 4.')

        break

      except ValueError:
        print(Fore.RED + 'Please enter a number between 0 and 4')
    tries += 1
    if currentComputer[moveRow][moveColumn] == '-' or currentComputer[moveRow][
        moveColumn] == 'X':
      currentComputer[moveRow][moveColumn] = 'X'
      fieldCommun[moveRow][moveColumn] = 'X'
      scores["player"] += 0

    else:
      currentComputer[moveRow][moveColumn] = '$'
      fieldCommun[moveRow][moveColumn] = '$'
      scores["player"] += 1

    print()
    print('**********************************')
    print(f'Player guessed: ({moveRow}, {moveColumn})')
    if fieldCommun[moveRow][moveColumn] == '$':

      print('Player hit a ship!')
      print('**********************************')
    else:

      print('Player missed this time.')
      print('**********************************')
    print()
    drawfield(fieldCommun)
    print('**********************************')
    moveRow = random.randint(0, 4)
    moveColumn = random.randint(0, 4)
    if currentPlayer[moveRow][moveColumn] == '-' or currentPlayer[moveRow][
        moveColumn] == 'X':
      currentPlayer[moveRow][moveColumn] = 'X'
      scores["computer"] += 0

    else:
      currentPlayer[moveRow][moveColumn] = '£'
      scores["computer"] += 1

    print(f'Computer guessed: ({moveRow}, {moveColumn})')
    if currentPlayer[moveRow][moveColumn] == '£':
      print('Computer hit a ship!')
    else:
      print('Computer missed this time.')

    print('**********************************')
    print()

    drawfield(currentPlayer)
    print()

    print(
      Fore.CYAN +
      f"After this round, The scores are: \n{name}: {scores['player']}.  Computer:  {scores['computer']}"
    )

    print()
    if tries < 5:
      while True:
        try:

          playAgain = input('Would you like to keep playing? (y/n)\n').lower()
          if playAgain != 'y' and playAgain != 'n':
            raise ValueError(Fore.RED + "Please enter 'y' or 'n'")
          elif playAgain == 'n':

            break
            anotherGame = False
          else:
            break

        except ValueError:
          print(Fore.RED + "Please enter 'y' or 'n'")
    else:
      print(Fore.RED + 'You have run out of tries!')

      print(
        Fore.CYAN +
        f"Finally, scores are: \n{name}: {scores['player']}.  Computer:  {scores['computer']}"
      )
      if scores['player'] > scores['computer']:
        print(Fore.GREEN + f"Congratulations {name}! You won!")
      elif scores['player'] < scores['computer']:
        print(Fore.RED + f"Sorry {name}, you lost!")
      else:
        print(Fore.YELLOW + "It is a DRAW!")
      break

  print()
  print('Thanks for playing!')
  print()
  drawfield(currentComputer)
  print('-------------------------')
  drawfield(currentPlayer)
  print()
  while True:
    if playAgain == 'n':      
      anotherGame = False
      break
    anotherGame = input('Would you like to play another game? (y/n)\n').lower()
    if anotherGame != 'y' and anotherGame != 'n':
      print(Fore.RED + "Please enter 'y' or 'n'")
    elif anotherGame == 'n':
      print(Fore.CYAN + 'Thanks for playing!')
      anotherGame = False
      break
    elif anotherGame == 'y':
      anotherGame = True
      break


  

  

