password = "code6a"
attempt = 3
while True:
    user = input("Enter username :")
    
    while attempt>0:
        user_password = input("Enter password :")
        if  user_password == password:
            print("Welcome to Account")
            break
        else:
            print("Try again")
        attempt-=1
        print(f"few {attempt} attempt")
        
    if attempt == 0:
       print("Your account has been block")
            