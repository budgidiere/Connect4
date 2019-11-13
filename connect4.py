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

line0 = [0, 0, 0, 0, 0, 0, 0, 0]
line1 = [0, 0, 0, 0, 0, 0, 0, 0]
line2 = [0, 0, 0, 0, 0, 0, 0, 0]
line3 = [0, 0, 0, 0, 0, 0, 0, 0]
line4 = [0, 0, 0, 0, 0, 0, 0, 0]
line5 = [0, 0, 0, 0, 0, 0, 0, 0]
line6 = [0, 0, 0, 0, 0, 0, 0, 0]
line7 = [0, 0, 0, 0, 0, 0, 0, 0]

array = [line7, line6, line5, line4, line3, line2, line1, line0]

done = False

def user1():
    printboard()
    done = False
    tmpuser1 = input("User 1 where would you like to go? ")
    tmpuser1 = int(tmpuser1)
    for item in array:
        print(item[tmpuser1])
        if item[tmpuser1] == 0:
            #print("here1")
            pass
        elif item[tmpuser1] != 0:
            #print("here2")
            if item == line7:
                line6[tmpuser1] == "X"
            elif item == line6:
                line5[tmpuser1] == "X"
            elif item == line5:
                line4[tmpuser1] == "X"
            elif item == line4:
                line3[tmpuser1] == "X"
            elif item == line3:
                line2[tmpuser1] == "X"
            elif item == line2:
                line1[tmpuser1] == "X"
            elif item == line1:
                line0[tmpuser1] == "X"
            elif item == line0:
                print("Invalid position try again.")
            else:
                user1()
            done = True
    if done != True:
        print("here")
        line7[tmpuser1] == "X"
    printboard()
            

def printboard():
    for item in array:
        print(item)

user1()
