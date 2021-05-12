low = 1
high = 1000

print("Please think of a number between {0} and {1}: ".format(low, high))
input("Press Enter to start")

guesses = 1
while low != high:
    print("\tGuessing in range {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {} should I guess higher or lower? "
                     "enter h or l or c if my guess was correct "
                     .format(guess).casefold())

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break

    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    guesses += 1
else:
    print("you thought of number {}".format(low))
    print("I got it in {} guesses".format(guesses))
