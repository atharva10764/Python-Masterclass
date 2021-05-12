day = "Saturday"
temperature = 35
raining = True

if day == "Saturday" and temperature < 37 or not raining:
    print("Go swimming")
else:
    print("read books")

if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name")
#if name:
if name != "":
    print("hello, {}".format(name))
else:
    print("Are you a man with no name")
