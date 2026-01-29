from income_manager import IncomeManager
from category_manager import CategoryManager

# Testing Income Manager
income = IncomeManager()
print(income.add_income(300, "Salary", "20-01-2026", "Weekend shift"))
print(income.add_income("", "Gift", "21-01-2026", "Birthday money"))
print(income.view_income())

# Testing Category Manager
categories = CategoryManager()
print(categories.view_categories())
print(categories.add_category("Gifts"))
print(categories.add_category("Food"))
print(categories.view_categories())
