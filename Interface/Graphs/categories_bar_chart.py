import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath('..'))
from MongoDB.T2_chart_data import retrieve_expense_data


def draw_T2_chart(date=None, budget=[]):
    # Define the categories and data
    categories = ["toll", "food", "parking", "transport", "accom", "gasoline", "telecom", "misc"]
    planned_budget = budget  # Planned Budget (bars)
    actual_expenses = retrieve_expense_data(date)  # Actual Expenses (line)

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

    # Check if the directory exists, and if not, create it
    output_path = r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\Interface\static\Trend_2.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path, bbox_inches='tight')
    print("Saved")

if __name__ == "__main__":
    draw_T2_chart()
