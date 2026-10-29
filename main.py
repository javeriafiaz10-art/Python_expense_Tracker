#1. Expense Tracker Project
expenses = [] #list of all expenses in form of dictionary 
print(" Welcome to expense tracker: ")

while True:
    print("=== MENU ====")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. view Totel spending")
    print("4. Exit")
    #ADD Expense

    choice = int(input("Please Enter Your Choice : "))
    if (choice == 1):
        date = input("Please Enter date")
        category = input("Please Enter the category")
        description = input("Please Enter detail")
        amount = float (input("Please Enter Your Amount"))
        expense={
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("\n Expense added successfully")

 #2. View all Expenses


    elif (choice == 2):
        if (len(expenses)==0):
            print("\n No expenses has been added yet. ")
        else:
            print("==== All Expense ====")
            count = 1
            for eachexpense in expenses:
                print(
                    f"expense no{count} ->"
                    f"{eachexpense["date"]}",
                    f"{eachexpense["category"]},"
                    f"{eachexpense["description"]},"
                    f"{eachexpense["amount"]}"
                    ) 
                count = count + 1   

    #3 . view total spending


    elif(choice == 3):
        total = 0
        for eachexpense in expenses:
            total = total + eachexpense["amount"]
        print("\n TOTAL SPENDING = " , total )
    
    #4. EXIT
    elif(choice == 4):
        print("Thank you for using the system")
        break
    else:
        print("INVALID CHOICE")
