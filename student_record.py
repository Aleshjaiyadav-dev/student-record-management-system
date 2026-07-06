def enter_details(a):
    details = int(input(f"Enter the Student's {a} :"))
    students_details[a] = details
students = []
while True:
    print("0  -> Exit the system")
    print("1  -> Add Student Selected")
    print("2  -> View Selected Student")
    print("3  -> Search Student Selected")
    try:
        option = int(input("Enter your choice :"))
    except ValueError:
            print("Enter integer only")
    if option == 0:
        break
    elif option == 1:
        students_details = {}
        print("Add Student Selected")
        details = input(f"Enter the Student's name :")
        students_details["name"] = details
        try:
            enter_details("roll_no")
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
        try:
            roll_search = int(input("Enter the roll_no To search :"))
        except ValueError:
            print("Enter integer only")
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
    else:
        print("Wrong choice ,Choose again")
print("Successfully exiter the Program")