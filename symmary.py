
choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose option from list below")
        print("1:\tLearn Python")
        print("2:\tGo to Eat")
        print("3.\tGo to Sleep")
        print("4:\tGet up")
        print("5:\tBrush your teeth")
        print("0:\tExit")

    choice = input()

