import json


class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }

class Tracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"Added: {expense.category} - ₹{expense.amount}")

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]
    
    def save_to_file(self, filename):
        data = [expense.to_dict() for expense in self.expenses]
        with open(filename, "w") as f:
            json.dump(data, f)
        print(f"Saved {len(data)} expenses to {filename}")

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        self.expenses = [Expense(d["amount"], d["category"], d["date"], d["description"]) for d in data]
        print(f"Loaded {len(self.expenses)} expenses from {filename}")

apple = Expense(200, "Food", "2026-07-03", "Bought apples")
petrol = Expense(500, "Transport", "2026-07-03", "Bike fuel")
print(apple.amount)
print(apple.category)
print(apple.date)
print(apple.description)

my_tracker = Tracker()
my_tracker.add_expense(apple)
my_tracker.add_expense(petrol)
print(my_tracker.total_expenses())
print(apple.to_dict())

food_expenses = my_tracker.expenses_by_category("Food")
for expense in food_expenses:
    print(expense.description, expense.amount)

my_tracker.save_to_file("expenses.json")

new_tracker = Tracker()
new_tracker.load_from_file("expenses.json")
print(new_tracker.total_expenses())