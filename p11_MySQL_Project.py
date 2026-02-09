import mysql.connector as mysql
conn = mysql.connect(
    host = "localhost",
    user = "root",
    password = "mysql",
    database = "python_db"
)
print("Connected!..")

def add_detail():
    cursor = conn.cursor()
    sql = "insert into students (id, name, age, course) values (%s,%s,%s,%s)"
    id = int(input("Enter ID:"))
    name = input("Enter name:").title()
    age = int(input("Enter age:"))
    course = input("Enter course:")
    record = (id, name, age, course)

    cursor.execute(sql,record)
    conn.commit()
    print("Record submit succussfully")

def show_details():
    cursor = conn.cursor()
    sql = "select * from students"
    cursor.execute(sql)
    records = cursor.fetchall()
    if records:
        print("ID\t Name\t Age\t Course")
        print("-"*30)
        for record in records:
            print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")
    else:
        print("Record not found!")

def search_detail():
    cursor = conn.cursor()
    sql = "select * from students where id = %s"
    id = int(input("Enter ID:"))
    cursor.execute(sql,(id,))
    record = cursor.fetchone()
    if record:
        print("\nStudent Details..")
        print("-"*17)
        print("ID     :",record[0])
        print("Name   :",record[1])
        print("Age    :",record[2])
        print("Course :",record[3])
    else:
        print("No record found!")

def update_detail():
    cursor = conn.cursor()
    sql = "update students set name = %s, age = %s, course = %s where id = %s"
    id = int(input("Enter ID:"))
    name = input("Enter new name:").title()
    age = int(input("Enter new age:"))
    course = input("Enter new course:")

    cursor.execute(sql,(name, age, course, id))
    conn.commit()
    if cursor.rowcount == 0:
        print("Record does not exist!")
    else:
        print("Record has been updated successfully")

def delete_detail():
    cursor = conn.cursor()
    sql = "delete from students where id = %s" 
    id = int(input("Enter ID:"))
    

    cursor.execute(sql,(id,))
    conn.commit()
    if cursor.rowcount != 0:
        print("Record has been deleted successfully") 
    else:
        print("Record does not exist!")


while True:
    print("\n==WelCome To Students Details==")
    print("1.Insert Student Detail")
    print("2.Veiw All Detail")
    print("3.Search Student Detail")
    print("4.Update Student Detail")
    print("5.Delete Student Detail")
    print("6.Exit\n")

    choice = int(input("Enter (1 to 6) number : "))

    if choice == 1:
        add_detail()
    elif choice == 2:
        show_details()
    elif choice == 3:
        search_detail()
    elif choice == 4:
        update_detail()
    elif choice == 5:
        delete_detail()
    elif choice == 6:
        print("Thank for visit")
        break
    else:
        print("Number is invalide")
