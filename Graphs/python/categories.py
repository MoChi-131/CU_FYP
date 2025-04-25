import matplotlib.pyplot as plt
import numpy as np

# Step 1: Define initial data
months = ['Jan', 'Feb', 'Mar', 'Apr']
gasoline = [20, 25, 30, 22]
food = [180, 175, 350, 160]
rent = [500, 510, 520, 505]
utilities = [200, 210, 230, 215]

# Step 2: Change a variable — e.g., update March food expense
food[2] = 300  # originally 350

# Step 3: Convert data for stacked bar
ind = np.arange(len(months))
width = 0.6

# Plotting stacked bar
p1 = plt.bar(ind, gasoline, width, color='blue', label='Gasoline')
p2 = plt.bar(ind, food, width, bottom=gasoline, color='red', label='Food')
p3 = plt.bar(ind, rent, width, bottom=np.array(gasoline) + np.array(food), color='skyblue', label='Rent')
p4 = plt.bar(ind, utilities, width, bottom=np.array(gasoline) + np.array(food) + np.array(rent), color='green', label='Utilities')

# Labels
plt.ylabel('Amount ($)')
plt.title('Expenses by Month')
plt.xticks(ind, months)
plt.legend(loc='upper right')
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()
