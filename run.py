#- - - - -
#- - - - -
#- - - - -
#- - - - -
#- - - - -

for row in range(5):
    for column in range(10):
        if column % 2 == 0:
            print("-", end="")
        else:
            print(" ", end="")
    print(" ")