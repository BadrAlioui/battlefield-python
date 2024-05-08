import random

#build a board

#0123456789
#- - - - - 0
#- - - - - 1
#- - - - - 2
#- - - - - 3
#- - - - - 4

import random

print('----------------------------------')
print(
  'Welcome to Ultimate BATTLESHIPS! !\nBoard size: 5. Number of ships : 4\nTop left corner is row:, col: 0'
)
print('----------------------------------')

name = input('Please enter your name: \n')
scores = {"computer": 0, "player": 0}


def drawfield(field):
  '''
    This function draws the field'''
  for row in range(5):
    for col in range(10):
      if col % 2 == 0:
        rightColumn = col // 2
        print(field[row][rightColumn], end="")
      else:
        print(" ", end="")
    print(' ')


currentPlayer = [list(('-') * 5) for i in range(5)]

currentComputer = [list(('-') * 5) for i in range(5)]

fieldCommun = [list(('-') * 5) for i in range(5)]


def random_number(gamer):
  '''
  This function generates a random number for the row and column'''
  for i in range(4):
    movecompRow = random.randint(0, 4)
    movecompColumn = random.randint(0, 4)
    if gamer == currentPlayer:
      currentPlayer[movecompRow][movecompColumn] = "@"
    else:
      currentComputer[movecompRow][movecompColumn] = "'"


random_number(currentPlayer)
random_number(currentComputer)

print()
print(f"{name}'s Board")
print()
drawfield(currentPlayer)
print()
print('----------')
print('Computer\'s Board: ')
print()

drawfield(fieldCommun)

print()
playAgain = 'y'
while playAgain == 'y':
  while True:
    try:
      moveRow = int(input("Guess a row between 0 and 4: \n"))
      moveColumn = int(input("Guess a column between 0 and 4: \n"))
      if moveRow < 0 or moveRow > 4 or moveColumn < 0 or moveColumn > 4:
        raise ValueError(
          'Invalid input. Please enter a number between 0 and 4.')

      break

    except ValueError:
      print('Please enter a number between 0 and 4')
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

  print(f'Player guessed: ({moveRow}, {moveColumn})')
  if fieldCommun[moveRow][moveColumn] == '$':
    print('Player hit a ship!')
  else:
    print('Player missed! this time.')
  print()
  drawfield(fieldCommun)
  print('-------------------------')
  moveRow = random.randint(0, 4)
  moveColumn = random.randint(0, 4)
  if currentPlayer[moveRow][moveColumn] == '-' or currentComputer[moveRow][
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
    print('Computer missed! this time.')

  print('-----------------------------')
  print()

  drawfield(currentPlayer)
  print()
  print(
    f"After this round, The score are: \n{name}: {scores['player']}.  Computer:  {scores['computer']}"
  )
  print()
  while True:
    try:
      playAgain = input('Would you like to keep playing? (y/n)\n').lower()
      if playAgain != 'y' and playAgain != 'n':
        raise ValueError("Please enter 'y' or 'n'")
      else:
        break
    except ValueError:
      print("Please enter 'y' or 'n'")

print()
print('Thanks for playing!')
print()
drawfield(currentComputer)
print('-------------------------')

drawfield(currentPlayer)
