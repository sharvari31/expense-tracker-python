import json
import streamlit as st

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

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def save_to_file(self, filename):
        data = [expense.to_dict() for expense in self.expenses]
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        self.expenses = [Expense(d["amount"], d["category"], d["date"], d["description"]) for d in data]

st.title("💰 Expense Tracker")

if "tracker" not in st.session_state:
    st.session_state.tracker = Tracker()

with st.form("add_expense_form"):
    amount = st.number_input("Amount", min_value=0.0, step=10.0)
    category = st.text_input("Category")
    date = st.date_input("Date")
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_expense = Expense(amount, category, str(date), description)
        st.session_state.tracker.add_expense(new_expense)
        st.success(f"Added {category} - ₹{amount}")

st.subheader("Your Expenses")
for expense in st.session_state.tracker.expenses:
    st.write(f"{expense.category}: ₹{expense.amount} — {expense.description}")

st.metric("Total Expenses", f"₹{st.session_state.tracker.total_expenses()}")