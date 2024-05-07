import random

#build a board

#0123456789
#- - - - - 0
#- - - - - 1
#- - - - - 2
#- - - - - 3
#- - - - - 4

print('----------------------------------')
print(
  'Welcome to Ultimate BATTLESHIPS! !\nBoard size: 5. Number of ships : 4\nTop left corner is row:, col: 0'
)
print('----------------------------------')

name = input('Please enter your name: \n')
scores = {"computer": 0, "player": 0}

def drawfield(field):
  for row in range(5):
    for col in range(10):
      if col % 2 == 0:
        rightColumn = col // 2
        print(field[row][rightColumn], end="")
      else:
        print(" ", end="")
    print(' ')

#create field for the player and the computer
currentPlayer = [list(('-') * 5) for i in range(5)]

currentComputer = [list(('-') * 5) for i in range(5)]

#to hide the field or the board of the computer
fieldCommun = [list(('-') * 5) for i in range(5)]

for i in range(4):
  movecompRow = random.randint(0, 4)
  movecompColumn = random.randint(0, 4)
  currentPlayer[movecompRow][movecompColumn] = "@"

for i in range(4):
  movecompRow = random.randint(0, 4)
  movecompColumn = random.randint(0, 4)
  currentComputer[movecompRow][movecompColumn] = "'"

print()
print(f"{name}'s Board")
drawfield(currentPlayer)
print()
print('----------')
print('Computer\'s Board: ')
print()

def field(field):
    '''
    board for the computer without showing the ships
    '''
for row in range(5):
  for col in range(10):
    if col % 2 == 0:
      rightColumn = col // 2

      print(fieldCommun[row][rightColumn], end="")
    else:
      print(" ", end="")
  print(' ')


field(fieldCommun)

for i in range(4):

  moveRow = int(input("Enter the row you want to move to: "))
  moveColumn = int(input("Enter the column you want to move to: "))
  if currentComputer[moveRow][moveColumn] == '-':
    currentComputer[moveRow][moveColumn] = 'X'
    fieldCommun[moveRow][moveColumn] = 'X'
    scores["player"] += 0
    print(
      f"The score is: {scores['computer']} for the computer and {scores['player']} for the player"
    )

  else:
    currentComputer[moveRow][moveColumn] = '$'
    fieldCommun[moveRow][moveColumn] = '$'
    scores["player"] += 1
    print(
      f"The score is: {scores['computer']} for the computer and {scores['player']} for the player"
    )
  field(fieldCommun)
  print('-------------------------')
  moveRow = random.randint(0, 4)
  moveColumn = random.randint(0, 4)
  if currentPlayer[moveRow][moveColumn] == '-':
    currentPlayer[moveRow][moveColumn] = 'X'
    scores["computer"] += 0
    print(
      f"The score is: {scores['computer']} for the computer and {scores['player']} for the player"
    )
  else:
    currentPlayer[moveRow][moveColumn] = '£'
    scores["computer"] += 1
    
    print(
      f"The score is: {scores['computer']} for the computer and {scores['player']} for the player"
    )

  drawfield(currentPlayer)

print()
drawfield(currentComputer)
print('-------------------------')

drawfield(currentPlayer)