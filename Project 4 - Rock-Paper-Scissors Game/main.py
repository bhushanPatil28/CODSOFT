import random 

print("Welcome to the Rock-Paper-Scissors Game")
print()
while True:
    user_choice = input("Please choose your action (Stone:1, Paper:2, Scissors:3)")

    try:
        user_choice = int(user_choice)
    except:
        print("Please choose from 1-3 numbers only")
        user_choice = input("Please choose your action (Stone:1, Paper:2, Scissors:3)")

    computer_choice = random.choice([1,2,3])

    if (computer_choice == 1 and user_choice == 2) or (computer_choice == 2 and user_choice == 3) or (computer_choice == 3 and user_choice == 1):
        print(F"You won, Yayyyy! Your choice : {user_choice}, computter choice : {computer_choice}")
    else: 
        print(F"You lost, Boooo! Your choice : {user_choice}, computter choice : {computer_choice}")
    
    running = input("Do you want to play again (Y/N)").lower()
    if running == "n":
        break

