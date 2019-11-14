import time

def begining():
    print("Welcome to Connect 4!")
    print("If you are new to Connect 4 (reproduced by Bud and Jonathan) press 1")
    print("If you are familiar with Connect 4 (reproduced by Bud and Jonathan press 2)")
    userinput = input("> ")
    if userinput == "1":
        print("")
    elif userinput == "2":
        print("Transporting to Game Zone")
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
    tmpuser = input("{} where would you like to go? ".format(player))
    tmpuser = int(tmpuser)
    for item in array:
        print(item[tmpuser])
        if item[tmpuser] == " ":
            #print("here1")
            pass
        elif item[tmpuser] != " ":
            #print("here2")
            if line7[tmpuser] == "X" or line7[tmpuser] == "Z":
                print("Invalid position try again.")
                place()
            elif line6[tmpuser] == "X" or line6[tmpuser] == "Z":
                line7[tmpuser] = player
                return
            elif line5[tmpuser] == "X" or line5[tmpuser] == "Z":
                line6[tmpuser] = player
                return
            elif line4[tmpuser] == "X" or line4[tmpuser] == "Z":
                line5[tmpuser] = player
                return
            elif line3[tmpuser] == "X" or line3[tmpuser] == "Z":
                line4[tmpuser] = player
                return
            elif line2[tmpuser] == "X" or line2[tmpuser] == "Z":
                line3[tmpuser] = player
                return
            elif line1[tmpuser] == "X" or line1[tmpuser] == "Z":
                line2[tmpuser] = player
                return
            elif line0[tmpuser] == "X" or line0[tmpuser] == "Z":
                line1[tmpuser] = player
                return
            done = True
    if done != True:
        print("here")
        
        line0[tmpuser] = player
        return
    printboard()
            

def printboard():
    for item in array:
        print(item)
    print(" ")

while True:
    place("X")
    place("Z")
