def add():
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))    
    print("Addition :",num1+num2) 
def sub():
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))    
    print("Subtraction :",num1-num2) 
def mul():
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))    
    print("Multiplication :",num1*num2) 
def div():
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))    
    print("Division :",num1/num2) 

while True:
    print("Choose 1 to 5")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choose=int(input("Enter 1 to 5 : "))
    if choose == 1:
        add()
    elif choose == 2:
        sub()
    elif choose == 3:
        mul()
    elif choose == 4:
        div()
    elif choose == 5:
        print("Exit")
        break
    else:
        print("Invalid Input")

    
    