def enter_details(a):
    details = int(input(f"Enter the Student's {a} :"))
    students_details[a] = details
    
def enter_rollno(a = ""):
    while True:
        try:
            b = int(input(a))
        except ValueError:
            print("Enter integer only")
        else:
            return b  
            break
def delete_record(roll_search):
            found = False
            for student in students:
                if roll_search == student["roll_no"]:
                    students.remove(student)
                    break
students = []
while True:
    roll_search,option = 0,0
    print("0  -> Exit the system")
    print("1  -> Add Student Selected")
    print("2  -> View Selected Student")
    print("3  -> Search Selected Student")
    print("4  -> Delete Selected Student")
    print("5  -> Update Selected Student")
    option = enter_rollno("Enter your Choice :")
    if option == 0:
        break
    elif option == 1:
        students_details = {}
        print("Add Student Selected")
        details = input("Enter the Student's name :")
        students_details["name"] = details
        try:
            details = int(input("Enter the Student's roll_no :"))
            found = False
            for student in students:
                if details == student["roll_no"]:
                    found = True
                    break
            if not found:
                students_details["roll_no"] = details
            else:
                print("Roll_no already present")
                continue
            enter_details("age")
            enter_details("marks")
        except ValueError:
            print("Enter integer only")
        students.append(students_details)
    elif option == 2:
        if not students:
            print("No student records found")
            continue
        print("View Student Selected")
        print("\n"+"=" * 30)
        print("    STUDENT RECORD SYSTEM")
        print("=" * 30 + "\n")
        for student in students:
            print("-" * 35)
            for key , value in student.items():
                print(f"{key : <10}: {value}")
    elif option == 3:
        roll_search = enter_rollno("Enter the roll_no of the student to be search :")
        found = False
        for student in students:
            if roll_search == student["roll_no"]:
                print("-" * 35)
                for key , value in student.items():
                    print(f"{key : <10}: {value}")
                    found = True
                break
        if not found:
            print("Searched roll_no is not found")
    elif option == 4:
        roll_search = enter_rollno("Enter the roll_no of the student to be Deleted :")
        delete_record(roll_search)
    elif option == 5:
        roll_search = enter_rollno("Enter the roll_no of the student to Update Record :")
        for student in students:
            if roll_search == student["roll_no"]:
                print("1  -> Name")
                print("2  -> Marks")
                print("3  -> Age")
                try:
                    update_option = int(input("Enter Your Choice :"))
                except ValueError:
                    print("Enter integer only")
                if update_option == 1:
                    update_changes = input("Enter the new Name")
                    student["name"] = update_changes
                elif update_option == 2:
                    update_changes = enter_rollno("Enter the new marks :")
                    student["marks"] = update_changes
                elif update_option == 3:
                    update_changes = enter_rollno("Enter the new Age :")
                    student["age"] = update_changes
    else:
        print("Wrong choice ,Choose again")
print("Successfully exiter the Program")