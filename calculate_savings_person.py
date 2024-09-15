# Prompt the user to enter their monthly income (as a float)
monthly_income = float(input("Enter the monthly income: "))
# Prompt the user to enter their total monthly expenses (as a float), which include rent, groceries, utilities, and other expenses
monthly_expenses = float(input("Enter the total monthly expenses: "))
# Calculate the total savings by subtracting the total expenses from the income
total_savings = monthly_income - monthly_expenses
# Calculate the percentage of income saved and the percentage of income spent
percentage_of_income_saved = (total_savings/monthly_income)*100
percentage_of_income_spent = (monthly_expenses/monthly_income)*100
# Display the total savings
print("Total Savings: ",total_savings)
# Display the percentage of income saved and spent, formatted to two decimal places
print(f"Percentage of income saved: {percentage_of_income_saved : .2f}")
print(f"Percentage of income saved: {percentage_of_income_spent: .2f}")
