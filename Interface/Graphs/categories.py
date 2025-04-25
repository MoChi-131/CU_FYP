import matplotlib.pyplot as plt
import numpy as np
import sys
import os

sys.path.append(os.path.abspath('..'))
from MongoDB.T1_chart_data import retrieve_expense_monthly_data
from MongoDB.T1_chart_data_weekly import retrieve_expense_data_weekly


def create_expense_plot(current_date=None, mode=None):
    # Retrieve data from MongoDB
    if mode == None or mode == "Monthly":
        data = retrieve_expense_monthly_data(current_date)
        x_label = data['months']  # Corrected typo from 'x_lable' to 'x_label'
    elif mode == "Weekly":
        data = retrieve_expense_data_weekly(current_date)
        x_label = data['week_labels']

    # Extract data
    category_data = data['category_data']
    categories = data['categories']
    stack_totals = data['stack_totals']
    start_date = data['start_date']
    end_date = data['end_date']

    # Calculate total for each category
    category_totals = {category: round(sum(category_data[category]), 2) for category in categories}

    # Define color palette (RGB)
    color_palette = [
        [1.0, 0.4, 0.4],
        [0.2, 0.6, 0.3],
        [0.8, 0.5, 0.2],
        [0.68, 0.85, 0.90],
        [0.7, 0.7, 0.7],
        [0.5, 0.5, 1.0],
        [1.0, 0.8, 0.2],
        [0.6, 0.4, 0.8]
    ]

    # Map categories to colors
    category_colors = dict(zip(categories, color_palette))

    # Set up plot
    ind = np.arange(len(x_label))
    width = 0.6
    fig, ax = plt.subplots()

    # Plot stacked bars and add segment labels
    bottom = np.zeros(len(x_label))
    for category in categories:
        amounts = category_data[category]
        ax.bar(
            ind,
            amounts,
            width,
            bottom=bottom,
            color=category_colors[category],
            label=category.capitalize()
        )

        # Add text labels for each segment (only if amount > 0)
        for i, amount in enumerate(amounts):
            if amount > 0:
                ax.text(
                    i,
                    bottom[i] + amount / 2, 
                    f'£{amount:.2f}',         # Only show this segment's amount
                    ha='center',
                    va='center',
                    fontsize=8,
                    color='white' if amount > 50 else 'black'
                )

        bottom += np.array(amounts)
        
    # Add text labels for stack totals
    for i, total in enumerate(stack_totals):
        ax.text(
            i,
            total + 10,  # Offset above the stack
            f'£{total:.2f}',
            ha='center',
            va='bottom',
            fontsize=10
        )

    # Labels and layout
    ax.set_ylabel('Amount (£)')
    ax.set_title(f'Expenses by {"Month" if mode == "Monthly" else "Week"} ({start_date.strftime("%d %b %Y")} - {end_date.strftime("%d %b %Y")})')
    ax.set_xticks(ind)
    ax.set_xticklabels(x_label)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    ax.grid(axis='y')

    # Adjust y-axis to fit text labels
    ax.set_ylim(0, max(stack_totals) * 1.2)  # Extra space for stack totals

    # Save the figure
    plt.tight_layout()
    save_path = r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\Interface\static\Trend_1.png"
    plt.savefig(save_path)
    plt.close()

if __name__ == "__main__":
    create_expense_plot(mode="Weekly")
