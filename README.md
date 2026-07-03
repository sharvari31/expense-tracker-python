# Expense Tracker (CLI)

A simple command-line expense tracker built in Python, focused on learning core OOP concepts: classes, objects, attributes, and file persistence.

## What it does

- Add expenses with amount, category, date, and description
- Calculate total expenses across all entries
- Filter expenses by category
- Save expenses to a JSON file and load them back later

## Concepts covered

- Classes vs. objects (`Expense`, `Tracker`)
- Constructors (`__init__`) and the difference between parameters and attributes
- `self` and object references vs. new object creation
- List comprehensions and generator expressions
- Reading and writing JSON files for data persistence

## Example usage

\`\`\`python
apple = Expense(200, "Food", "2026-07-03", "Bought apples")
petrol = Expense(500, "Transport", "2026-07-03", "Bike fuel")

tracker = Tracker()
tracker.add_expense(apple)
tracker.add_expense(petrol)

print(tracker.total_expenses())  # 700

tracker.save_to_file("expenses.json")

new_tracker = Tracker()
new_tracker.load_from_file("expenses.json")
print(new_tracker.total_expenses())  # 700
\`\`\`

## Why this project

Built as Phase 0 of a hands-on path toward Generative AI engineering — starting from core Python/OOP fundamentals before moving into embeddings, RAG, and agents.