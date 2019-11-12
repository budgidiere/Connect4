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

line0 = []
line1 = []
line2 = []
line3 = []
line4 = []
line5 = []
line6 = []
line7 = []

array = [line0, line1, line2, line3, line4, line5, line6 ,line7]

def connect4():
    pass