class ATM :
    def __init__(self,account_no,account_holder,pin,amount=10000):
        self.account_no = account_no
        self.account_holder = account_holder
        self.pin = pin
        self.balance = amount

    def check_balance(self):
        print(f"Total balance : {self.balance}\n")

    def deposit(self,amt):
        self.balance+=amt
    
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient balance\n")
        else:
            self.balance-=amt
            print(f"Collect your cash : {amt}\n")
      
    def show_detail(self):
        print("Welcome to Sir")
        print("Holder account no. :",self.account_no)
        print("Account holder name :",self.account_holder)
        print()
        
A1 = ATM(123 , "Sachin Kumar" , "@sigma6v")
while True:
    print("=*=Welcome To ATM=*=")
    print("1.Check balance")
    print("2.Deposit amount")
    print("3.Withdraw amount")
    print("4.User details")
    print("5.Exit\n")

    choice = int(input("Write 1 to 5 buttom :"))
    print()
    if choice == 1:
        A1.check_balance()
    elif choice == 2:
        amount = int(input("Enter deposit amount = "))
        A1.deposit(amount)
    elif choice == 3:
        amount = int(input("Enter withdraw amount = "))
        A1.withdraw(amount)
    elif choice == 4:
        A1.show_detail()
    elif choice == 5 :
        break
    else:
        print("Please Enter right number!\n")