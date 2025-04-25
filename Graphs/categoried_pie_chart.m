% Data for the pie chart (percentages)
data = [5, 40, 20, 25, 10]; % 5% Parking, 40% Accommodation, 20% Gasoline, 25% Food, 10% Other

% Labels for the categories
labels = {'5% Parking', '40% Accommodation', '20% Gasoline', '25% Food', '10% Other'};

% Create the pie chart
figure;
h = pie(data, labels);

% Customize the title
title('Spending Category', 'FontSize', 14, 'FontWeight', 'bold');

% Add the total spending in the center
total = 439.74; % Total spending in pounds
text(0, 0, sprintf('TOTAL:\n£%.2f', total), ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle', ...
    'FontSize', 12, 'FontWeight', 'bold');

% Customize colors for all categories
colormap([0.9 0.4 0.4; ... % Red for Parking
          0.2 0.6 0.3; ... % Green for Accommodation
          0.8 0.5 0.2; ... % Orange for Gasoline
          0.68 0.85 0.90; ... % Light blue for Food (as requested earlier)
          0.7 0.7 0.7]); % Gray for Other