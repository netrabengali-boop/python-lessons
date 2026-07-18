import random
while True:
    users_choise = input("rock,paper,siscissors:")
    possible_choices = ["rock","paper","siscissors"]
    computer_choice = random.choice(possible_choices)
    print(f"You chose: {users_choise}")
    print(f"Computer chose: {computer_choice}")
    if users_choise == computer_choice:
       print("Its a tie")
    elif users_choise == "rock" and computer_choice == "siscissors":
        print("You win!")
    elif users_choise == "paper" and computer_choice == "rock":
        print("You win!")
    elif users_choise == "siscissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("you lose")