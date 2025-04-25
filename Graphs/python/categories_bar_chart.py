import matplotlib.pyplot as plt

# Define the categories and data
categories = ['Rent', 'Food', 'Transport', 'Entertainment', 'Savings']
planned_budget = [1200, 400, 200, 200, 300]  # Planned Budget (bars)
actual_expenses = [1200, 500, 200, 300, 200]  # Actual Expenses (line)

# Create the bar chart for Planned Budget
plt.figure(figsize=(8, 6))
plt.bar(categories, planned_budget, color=[0.7, 0.8, 1.0], label='Planned Budget')  # Light blue bars

# Overlay the line for Actual Expenses
plt.plot(categories, actual_expenses, 'r-o', linewidth=2, markersize=8, label='Actual Expenses')  # Red line with circles

# Customize the title and labels
plt.title('Planned Budget vs Actual Expenses', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Category')
plt.ylabel('Amount (£)')

# Add a legend
plt.legend(loc='upper right')

# Ensure the y-axis starts at 0
plt.ylim(0, max(max(planned_budget), max(actual_expenses)) * 1.1)  # Add some padding at the top

# Show x-axis grid lines (vertical lines at each category)
plt.grid(True, which='major', axis='y', linestyle='--', color='gray', alpha=0.7)

# Display the plot
plt.show()