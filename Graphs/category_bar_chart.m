% Define the categories and data
categories = {'Rent', 'Food', 'Transport', 'Entertainment', 'Savings'};
planned_budget = [1200, 400, 200, 200, 300]; % Planned Budget (bars)
actual_expenses = [1200, 500, 200, 300, 200]; % Actual Expenses (line)

% Create a numerical index for the x-axis (1, 2, 3, ...)
x = 1:length(categories);

% Create the bar chart for Planned Budget
figure;
bar(x, planned_budget, 'FaceColor', [0.7, 0.8, 1.0]); % Light blue color for bars

% Hold the plot to overlay the line
hold on;

% Plot the Actual Expenses as a line with markers using the numerical x-axis
plot(x, actual_expenses, 'r-', 'LineWidth', 2, 'MarkerSize', 8); % Red line with circles
set(gca, 'XGrid', 'off', 'YGrid', 'on'); % XGrid off, YGrid on

% Set the x-axis tick labels to the category names
xticks(x);
xticklabels(categories);

% Customize the title and labels
title('Planned Budget vs Actual Expenses', 'FontSize', 14, 'FontWeight', 'bold');
xlabel('Category');
ylabel('Amount (£)');

% Add a legend
legend('Actual Expenses', 'Planned Budget', 'Location', 'northeast');

% Ensure the y-axis starts at 0
ylim([0, max(max(planned_budget), max(actual_expenses)) * 1.1]); % Add some padding at the top

% Hold off to finish plotting
hold off;