#----------add this code to menu----------
def set_monthly_budget(username):
    month = input("Enter month (YYYY-MM): ")
    budget = float(input("Enter your monthly budget: "))
    with open("budgets.txt", "a") as file:
        file.write(f"{username},{month},{budget}\n")
    print("Monthly budget saved.")

# Function to add an expense and check budget
def add_expense(username):
    month = input("Enter month (YYYY-MM): ")
    category = input("Enter expense category: ")
    amount = float(input("Enter amount spent (£): "))  # UK pounds

    # Save the new expense
    with open("expenses.txt", "a") as file:
        file.write(f"{username},{month},{category},{amount}\n")

    # Calculate total expenses for the month
    total_spent = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                user, exp_month, _, exp_amount = line.strip().split(",")
                if user == username and exp_month == month:
                    total_spent += float(exp_amount)
    except FileNotFoundError:
        pass

    # Gives the budget for the month
    budget = None
    try:
        with open("budgets.txt", "r") as file:
            for line in file:
                user, bud_month, bud_amount = line.strip().split(",")
                if user == username and bud_month == month:
                    budget = float(bud_amount)
                    break
    except FileNotFoundError:
        pass

    # Alerts the users if they go over budget
    if budget is not None:
        if total_spent > budget:
            print(f"\nWARNING!: You have gone OVER your budget for {month}!")
            print(f"Budget: £{budget:.2f}")
            print(f"Total Spent: £{total_spent:.2f}")
        else:
            remaining = budget - total_spent
            print(
                f"\nExpense added. You have £{remaining:.2f} remaining this month."
            )
    else:
        print("\nExpense added. No budget is set for this month.")
