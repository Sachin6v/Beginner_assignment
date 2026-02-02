import random

user_score = computer_score =0
round = 0
while True:
    user_sum = computer_sum = 0
    computer = random.randint(1,6) , random.randint(1,6)
    user = int(input("Enter first Dice number (1 to 6) = ")),\
           int(input("Enter second Dice number (1 to 6) = "))
    print()
    print(f"user choose : {user}")
    print(f"computer choose :{computer}")
    for r in user:
        user_sum+=r
    for o in computer:
        computer_sum+=o
    if user_sum > computer_sum :
        print(f"User winner : {user_sum}\n")
        user_score+=1
    elif computer_sum > user_sum :
        print(f"Computer winner : {computer_sum}\n")
        computer_score+=1
    else:
        print("Match Tie\n")
    round+=1
    print(f"Round {round} complete")
    print(f"User score = {user_score}")
    print(f"Computer score = {computer_score}\n")
 