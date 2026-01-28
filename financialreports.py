def financial_report(username):
    # this is asking the user which month they want the report for
    month = input("Enter month (YYYY-MM): ")

    # the variables to keep track of totals
    total_spent = 0
    budget = 0
    found_budget = False  # this is used to check if a budget has already been made

    # the variables for the expense category
    food = 0
    transport = 0
    entertainment = 0
    other = 0

    # this is to find the user's budget for the selected month
    try:
        file = open("budgets.txt", "r")
        for line in file:
            parts = line.strip().split(",")  # split the line into parts
            # check if the username and month match
            if parts[0] == username and parts[1] == month:
                budget = float(parts[2])  # get the budget amount
                found_budget = True
        file.close()
    except FileNotFoundError:
        # runs if the budgets file does not exist
        print("No budget file found")

    # read the expenses file and add up spending
    try:
        file = open("expenses.txt", "r")
        for line in file:
            parts = line.strip().split(",")
            # check if expense belongs to this user and month
            if parts[0] == username and parts[1] == month:
                amount = float(parts[3])  # get the expense amount
                total_spent += amount  # add to total spent

                # add the amount to the correct category
                if parts[2] == "food":
                    food += amount
                elif parts[2] == "transport":
                    transport += amount
                elif parts[2] == "entertainment":
                    entertainment += amount
                else:
                    other += amount
        file.close()
    except FileNotFoundError:
        # this shows if the expenses file does not exist
        print("No expenses file found")

    # this can print the financial report for the user to see after the program has run 
    print("\n--- Financial Report ---")
    print("Month:", month)

    # this is to show the budget if it was found
    if found_budget:
        print("Budget: £", round(budget, 2))
    else:
        print("No budget set")

    # this shows how much was spent in total
    print("Total spent: £", round(total_spent, 2))

    # compares spending with budget
    if found_budget:
        if total_spent > budget:
            print("You are over budget by £", round(total_spent - budget, 2))
        else:
            print("Money left: £", round(budget - total_spent, 2))

    # prints a breakdown of expenses by category
    print("\nCategory breakdown:")
    if food > 0:
        print("Food: £", round(food, 2))
    if transport > 0:
        print("Transport: £", round(transport, 2))
    if entertainment > 0:
        print("Entertainment: £", round(entertainment, 2))
    if other > 0:
        print("Other: £", round(other, 2))
