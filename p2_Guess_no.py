import random
print("**Welcome to Game!**")
print("Exit game enter '0'\n")
user_high = computer_high = 0
user_low = computer_low = 0
round = 0
while True:
    computer_guess = random.randint(1,10)
    user =int(input("Enter the 1 to 10 :"))
    print()
    if user==0:
        break
    if 0<=user<=10:
        print("User guess no :",user)
        print("Computer guess no :",computer_guess)
    else:
        print("Try again Pls")

    if user > computer_guess:
        print("User high\n")
        user_high+=1
        computer_low+=1
    elif computer_guess > user:
        print("computer high\n")
        computer_high+=1
        user_low+=1
    else:
        print("Both are Equal\n")

    round+=1
    print(f"user high score {user_high}\nuser low score {user_low}\n")
    print(f"computer high score {computer_high}\ncomputer low score {computer_low}\n")
    print(f"Round {round} complete\n")

if user_high > computer_high :
    print("User won")
else:
    print("Computer won")

