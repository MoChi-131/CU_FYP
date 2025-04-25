import matplotlib.pyplot as plt

# Define the data and category names as variables (you can change these anytime)
data = [5, 40, 20, 25, 10]  # Percentages for each category
categories = ['Parking', 'Accommodation', 'Gasoline', 'Food', 'Other']

# Ensure the number of categories matches the number of data points
if len(data) != len(categories):
    raise ValueError('The number of data points must match the number of categories.')

# Dynamically create labels by combining percentages with category names
labels = [f'{percentage}% {category}' for percentage, category in zip(data, categories)]

# Create the pie chart
fig, ax = plt.subplots()

# Define a color palette to match the chart in the image
color_palette = [
    [1.0, 0.4, 0.4],  # Red for Parking
    [0.2, 0.6, 0.3],  # Green for Accommodation
    [0.8, 0.5, 0.2],  # Orange for Gasoline
    [0.68, 0.85, 0.90],  # Light blue for Food
    [0.7, 0.7, 0.7],  # Gray for Other
]

# Apply colors based on the number of categories and set startangle to 90
num_categories = len(data)
wedges, texts = ax.pie(
    data,
    labels=labels,
    colors=color_palette[:num_categories],
    startangle=90,  # Start at the middle top (12 o'clock position)
    counterclock=False  # Rotate clockwise
)

# Customize the title
plt.title('Spending Category', fontsize=14, fontweight='bold', pad=20)

# Add the total spending in the center
total = 439.74  # Total spending in pounds
plt.text(0, 0, f'TOTAL:\n£{total:.2f}', 
         horizontalalignment='center', 
         verticalalignment='center', 
         fontsize=12, 
         fontweight='bold')

# Ensure the pie chart is circular
ax.axis('equal')

# Display the chart
plt.show()