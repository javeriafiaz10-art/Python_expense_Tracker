student = {}

while True:
    print("\n------STUDENTS MANAGER APP------")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Check result")
    print("4. Check Attendance")
    print("5. Exit")

    choice = input("Enter Your Choice:  ")
    #Add student

    if choice == "1":
        name = input("Enter your Name: ")
        marks = int(input("Enter Marks: "))
        student[name] = marks
        print(f" {name} Successfully Added!")
    #View Students
    elif choice == "2":
        if not student:
            print("No Student found!")
        else:
            for name, marks in student.items():
                print(name,":", marks)
    #check result
    elif choice == "3":
        name = input("Enter your name: ")
        if name in student:
            marks = student[name]
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")

            
        else:
                print("Student Not Found!")        





    