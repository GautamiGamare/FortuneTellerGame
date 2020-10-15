print("Welcome to fortune telling game !!")
ans = True
while ans:
    color = input("Select Yellow, Green, Blue, Violet")
    if color == "Yellow" or color == "yellow" or color == "YELLOW" or color == "Blue" or color == "blue" or color == "BLUE":
        number = int(input("Select one number between (1,3,5,7,9)"))
        if number == 1:
            print("Worried about your future carrier? Don't worry you will 100% get what you want but br patient")
        elif number == 3:
            print("You will become millioner after 2 years")
        elif number == 5:
            print("You will have great family with 10 kids!")
        elif number == 7:
            print("You will become famous and everyone will love you")
        elif number == 9:
            print("You will get your dream job and all your dreams will come true")
        else:
            print("Please select from 1,3,5,7,9 numbers only")

    elif color == "Green" or color == "green" or color == "GREEN" or color == "Violet" or color == "violet" or color == "VIOLET":
        number = int(input("Select one number between (2,4,6,8)"))
        if number == 2:
            print("You will live happy life for 100 years at least")
        elif number == 4:
            print("You will become a successful doctor one day")
        elif number == 6:
            print("You are lucky!! you will have it all one day")
        elif number == 8:
            print("You will become a successful Singer one day")
        else:
            print("Please select from 2,4,6,8 numbers only")
    else:
        print("Please select from Yellow, Green, Blue, Violet only")
    ch=input("Continue Playing? Type Yes or else type No")
    if ch == "Yes" or ch == "yes" or ch == "YES":
        ans = True
    else:
        ans = False
