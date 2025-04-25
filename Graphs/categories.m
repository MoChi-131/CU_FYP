
% Categories: Gasoline, Food, Rent, Utilities
% Data for Jan, Feb, Mar, Apr
data = [
    20, 180, 500, 200;  % January
    25, 175, 510, 210;  % February
    30, 350, 520, 230;  % March
    22, 160, 505, 215   % April
];

% Transpose for stacked bar format (each row = category)
data = data';

% Month labels
months = {'Jan', 'Feb', 'Mar', 'Apr'};

% Category labels for legend
category = {'Parking', 'Food', 'Accommodation', 'Gasoline'};

% Create stacked bar chart
figure;
bar(data', 'stacked');

% Add labels
title('Expenses by Month');
xlabel('Month');
ylabel('Amount (£)');
set(gca, 'XTickLabel', months);
legend(category, 'Location', 'northeastoutside');

% Optional: improve appearance
grid on;
