def add_student():
    roll = int(input("Enter Student Roll no : "))
    name = input("Enter Student name : ").title()
    branch = input("Enter Student branch : ")
    with open("College Info.txt","a") as file:
        file.write(f"{roll},{name},{branch}\n")
def show_students():
    with open("College Info.txt") as file:
        for r in file:
         print(r, end="")
def search_student_roll_no():
    roll_no = input("Enter Roll No to search: ")
    found = False

    with open("College Info.txt", "r") as f:
        for line in f:
            roll, name, branch = line.strip().split(",")
            if roll == roll_no:
                print(f"Found → {roll}, {name}, {branch}")
                found = True
                break

    if not found:
        print("Student not found.")
def delete_recode_id():
    roll_no = input("Enter Roll No to search: ")
    content=[]

    with open("College Info.txt", "r") as f:
        content = f.readlines()
    with open("College Info.txt","w") as f:
        for line in content:
         roll, name, branch = line.strip().split(",")
         if roll != roll_no:
            content = f.write(line)
        else:
            print("Student ID not found.")

 

while True:
    print("\nWelcome To College\n")
    print("1.Add Recode Student")
    print("2.View All Recode")
    print("3.Search Student Recode")
    print("4.Delete student Recode")
    print("5.Exit\n")

    choice = int(input("Enter (1 to 5) number : "))
    print()
    if choice == 1:
        add_student()
    elif choice == 2:
        show_students()
    elif choice == 3:
        search_student_roll_no()
    elif choice == 4:
        delete_recode_id()
    elif choice == 5:
        break
    else:
        print("Invaild choose try again!")