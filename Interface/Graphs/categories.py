import matplotlib.pyplot as plt
import numpy as np
import os
from MongoDB import retrieve_expense_monthly_data, retrieve_expense_data_weekly


def create_expense_plot(current_date=None, mode=None, categories=[]):
    # Retrieve data from MongoDB
    if mode == None or mode == "Monthly":
        data = retrieve_expense_monthly_data(current_date, categories)
        x_label = data['months']  # Corrected typo from 'x_lable' to 'x_label'
    elif mode == "Weekly":
        data = retrieve_expense_data_weekly(current_date, categories)
        x_label = data['week_labels']

    # Extract data
    category_data = data['category_data']
    categories = data['categories']
    stack_totals = data['stack_totals']
    start_date = data['start_date']
    end_date = data['end_date']

    # Define color palette (RGB)
    color_palette = [
        [1.0, 0.4, 0.4],  # Reddish
        [0.2, 0.6, 0.3],  # Greenish
        [0.8, 0.5, 0.2],  # Orangish
        [0.68, 0.85, 0.90],  # Light blue
        [0.7, 0.7, 0.7],  # Gray
        [0.5, 0.5, 1.0],  # Blue
        [1.0, 0.8, 0.2],  # Yellowish
        [0.6, 0.4, 0.8],  # Purple
        [0.9, 0.3, 0.6]   # Pinkish
    ]

    # Map categories to colors
    category_colors = dict(zip(categories, color_palette))

    # Set up plot
    ind = np.arange(len(x_label))
    width = 0.6
    fig, ax = plt.subplots(figsize=(10, 6))

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
    plt.subplots_adjust(left=0.05, right=0.75, top=0.9, bottom=0.1)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.getenv("OUTPUT_PATH") or os.path.join(current_dir, '..', 'static', 'Trend_1.png')
    plt.savefig(save_path, dpi=300)
    plt.close()

if __name__ == "__main__":
    create_expense_plot(mode="Weekly")
