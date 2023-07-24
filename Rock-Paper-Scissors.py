import random

Wins = 0
Losses = 0
Ties = 0

while True:
    user_choice = input ("Choose between Rock, Paper, Scissors: ")
    
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f"You chose {user_choice}, Computer chose {computer_choice}.\n")

    if user_choice.lower() == computer_choice:
        print(f"Both players selected {user_choice.lower()}. It's a tie!")
        Ties +=1
        
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            print(f"Rock smashes scissors! You Dominated!")
            Wins +=1
        else:
            print("Paper covers rock! You Were Defeated!?")
            Losses +=1
        
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You Dominated!")
            Wins +=1
        else:
            print("Scissors cuts paper! You Were Defeated!?")
            Losses +=1
        
    elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You Dominated!")
            Wins +=1
        else:
            print("Rock smashes scissors! You Were Defeated!?")
            Losses +=1

    print(f"Wins: {Wins}")
    print (f"Losses: {Losses}")
    print(f"Ties: {Ties}")