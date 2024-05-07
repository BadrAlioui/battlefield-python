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