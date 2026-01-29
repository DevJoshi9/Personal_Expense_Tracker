class IncomeRecord:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"{self.date} | £{self.amount} | {self.category} | {self.description}"


class IncomeManager:
    def __init__(self):
        self.income_list = []

    def add_income(self, amount, category, date, description):
        if amount == "" or category == "" or date == "":
            return "Error: Missing required fields."

        record = IncomeRecord(amount, category, date, description)
        self.income_list.append(record)
        return "Income added successfully."

    def view_income(self):
        if not self.income_list:
            return "No income records found."

        output = "---- Income Records ----\n"
        for record in self.income_list:
            output += str(record) + "\n"
        return output
