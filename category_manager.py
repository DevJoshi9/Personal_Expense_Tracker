class CategoryManager:
    def __init__(self):
        self.categories = ["Food", "Transport", "Leisure"]

    def view_categories(self):
        return "Categories: " + ", ".join(self.categories)

    def add_category(self, name):
        name = str(name).strip()
        if name == "":
            return "Error: Category name cannot be empty."

        if name in self.categories:
            return "Category already exists."

        self.categories.append(name)
        return "Category added successfully."
