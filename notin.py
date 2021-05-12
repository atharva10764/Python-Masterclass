activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():
    print("But I want to go to cinema")
else:
    print("I want to go swimming")

name = input("Please enter your name")
age = int(input("How old are you?"))

if 18 <= age <= 31:
    print("Welcome to Holiday, {}".format(name))
else:
    print("Sorry, you are not invited")


