print("Welcome to Connect 4!")
print("If you are new to Connect 4 (reproduced by Bud and Jonathan) press 1")
print("If you are familiar with Connect 4 (reproduced by Bud and Jonathan press 2)")
userinput = input("> ")

line0 = [0, 0, 0, 0, 0, 0, 0, 0]
line1 = [0, 0, 0, 0, 0, 0, 0, 0]
line2 = [0, 0, 0, 0, 0, 0, 0, 0]
line3 = [0, 0, 0, 0, 0, 0, 0, 0]
line4 = [0, 0, 0, 0, 0, 0, 0, 0]
line5 = [0, 0, 0, 0, 0, 0, 0, 0]
line6 = [0, 0, 0, 0, 0, 0, 0, 0]
line7 = [0, 0, 0, 0, 0, 0, 0, 0]

array = [line0, line1, line2, line3, line4, line5, line6 ,line7]

def connect4():
    printboard()
    tmpuser1 = input("User 1 where would you like to go? ")

def printboard():
    for item in array:
        print(item)

connect4()
