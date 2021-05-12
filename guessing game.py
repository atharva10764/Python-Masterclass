import random

highest = 1000
answer = random.randint(1, highest)
print(answer) #TODO:remove after testing
print("Please guess number between 1 and {}: ".format(highest))

guess = 0 #initiate any number not equal to answer
while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it correctly")
        break

    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it correctly")
        # else:
        #     print("Sorry, you have not guessed correctly")



# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry,not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry,not guessed correctly")
# else:
#     print("guessed correctly")
#
