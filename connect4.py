import time

def begining():
    print("Welcome to Connect 4!")
    time.sleep(2)
    print("If you are new to Connect 4 (reproduced by Bud and Jonathan) press 1")
    print("If you are familiar with Connect 4 (reproduced by Bud and Jonathan press 2)")
    userinput = input("> ")
    if userinput == "1":
        print("Welcome to the rules.")
        time.sleep(2)
        print("As you will see when you begin, the game board consists of a 8x8 grid of boxes, each collumm is marked with a number (1-8).")
        time.sleep(4)
        print("To place a piece type the number that corresponds to the row that you wish to play into.")
        time.sleep(3)
        print("This is a two player game, each player will alternate placing pieces, one piece at a time.")
        time.sleep(3)
        print("To win, create a linear chain of four pieces horizontally, vertically, or diagonally.")
        time.sleep(3)
    elif userinput == "2":
        print("Transporting to Game Zone")
        time.sleep(2)
    else:
        begining()

begining()

line0 = [" ", " ", " ", " ", " ", " ", " ", " "]
line1 = [" ", " ", " ", " ", " ", " ", " ", " "]
line2 = [" ", " ", " ", " ", " ", " ", " ", " "]
line3 = [" ", " ", " ", " ", " ", " ", " ", " "]
line4 = [" ", " ", " ", " ", " ", " ", " ", " "]
line5 = [" ", " ", " ", " ", " ", " ", " ", " "]
line6 = [" ", " ", " ", " ", " ", " ", " ", " "]
line7 = [" ", " ", " ", " ", " ", " ", " ", " "]

array = [line7, line6, line5, line4, line3, line2, line1, line0]

done = False

def place(player):
    printboard()
    done = False
    tmpuser = input("{}, please select a collumn. ".format(player))
    tmpuser = int(tmpuser) - 1
    for item in array:
        print(item[tmpuser])
        if item[tmpuser] == " ":
            #print("here1")
            pass
        elif item[tmpuser] != " ":
            #print("here2")
            if line7[tmpuser] == "X" or line7[tmpuser] == "O":
                print("Invalid positioning, please try again.")
                
            if line7[tmpuser] == "X" or line7[tmpuser] == "O":
                print("Invalid positioning, please try again.")
                place(player)
                return
            elif line6[tmpuser] == "X" or line6[tmpuser] == "O":
                line7[tmpuser] = player
                return
            elif line5[tmpuser] == "X" or line5[tmpuser] == "O":
                line6[tmpuser] = player
                return
            elif line4[tmpuser] == "X" or line4[tmpuser] == "O":
                line5[tmpuser] = player
                return
            elif line3[tmpuser] == "X" or line3[tmpuser] == "O":
                line4[tmpuser] = player
                return
            elif line2[tmpuser] == "X" or line2[tmpuser] == "O":
                line3[tmpuser] = player
                return
            elif line1[tmpuser] == "X" or line1[tmpuser] == "O":
                line2[tmpuser] = player
                return
            elif line0[tmpuser] == "X" or line0[tmpuser] == "O":
                line1[tmpuser] = player
                return
            done = True
    if done != True:
        
        
        line0[tmpuser] = player
        return
    printboard()
def checkwinner():
    
def checkHV():
 
def fliparray():
    
      
            
>>>>>>> Stashed changes
def winner(player):
    print("Congratulations, {}, has won.".format(player))
    print("")
    print("   ----------    ")
    print("  -          -   ")
    print("   -        -    ")
    print("    -      -     ")
    print("     -    -      ")
    print("      -  -       ")
    print("      -  -       ")
    print("       --        ")
    print("      ----       ")
    print("    --------     ")
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

def printboard():
    print("['1', '2', '3', '4', '5', '6', '7', '8']")
    for item in array:
        print(item)
    print(" ")

while True:
    checkwinner()
    if gameover != True:
        place("X")
        place("O")
    else:
        winner()
