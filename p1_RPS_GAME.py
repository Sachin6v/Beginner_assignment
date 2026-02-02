import random
print("Welcome to Game")
print("Can't interst this game pls 'exit'\n")
lst = ["rock","paper","scissors"]

round = 0
ch_round = str_round = 0
while True:
    ch = random.choice(lst)
    str = input("User choose:").lower()
    if str=="exit":
        break
    if str == "rock" or str == "paper" or str == "scissors" : 
        print("Computer choose :",ch)
    else:
        print("Invaild string try again")

    if (ch=="rock" and str=="paper") or (ch=="scissors" and str=="paper") or (ch=="rock" and str=="scissors"):
        print("Computer win")
        ch_round+=1
    
    elif (ch=="paper" and str=="rock") or (ch=="paper" and str=="scissors") or (ch=="scissors" and str=="rock"):
        print("User win")
        str_round+=1
    
    else:
        print("Match Draw\n")
    round+=1    

    print(f"computer score {ch_round}\nUser score {str_round}")
    print(f"Round {round} complete\n")