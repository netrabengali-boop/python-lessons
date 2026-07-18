import random
playing=True
number=random.randint(0,9)
print("Welcome to the number guessing game!")
print("the computer has selected a number between 0 and 9. You have to guess it.")
while playing:
    guess=int(input("Enter a number: "))
    if guess==number:
        print("You guessed the nuber right!")
        break
    else:
        print("Give it another try")