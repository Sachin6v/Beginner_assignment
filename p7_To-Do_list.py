lst = []
while True:
    print("== Welcome To-Do List ==")
    print("1.Task add karna")
    print("2.Task delete karna")
    print("3.Task show karna")
    print("4.Exit\n")

    choice = int(input("Enter 1 to 4 buttom :"))

    if choice == 1:
        lst.append(input("Add any thing in lst :"))
        print()
    elif choice == 2:
        lst.remove(input("Remove in lst :"))
        print()
    elif choice == 3:
        print(f"Your list = {lst}")
        print()
    elif choice == 4:
        print("Thankyou! For Exit\n")
        break


