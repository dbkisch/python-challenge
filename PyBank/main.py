# PyBank
# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []
months_list = []
firstrow = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    firstrow = next(reader)

    # Initialize variables to track the total net profit, total months, and last profit to calculate net change
    total_net = int(firstrow[1])
    total_months = 1
    last_profit = int(firstrow[1])
 
    # Process each row of data
    for row in reader:
        month = str(row[0])
        profit = int(row[1])
        
        # Track the totals
        total_net += profit
        total_months = total_months + 1

        # Track the net change
        net_change = profit - last_profit
        
        # Add row to months list
        months_list.append(month)

        # Add row to net change list
        net_change_list.append(net_change)
      
        # Reset last_profit to current profit
        last_profit = profit
        
        # Calculate the greatest increase in profits (month and amount)          
        greatest_increase = max(net_change_list)
        incr_index = net_change_list.index(greatest_increase)
        month_greatest_increase = str(months_list[incr_index])

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(net_change_list)
        dec_index = net_change_list.index(greatest_decrease)
        month_greatest_decrease = str(months_list[dec_index])

# Calculate the average net change across the months using built-in functions
average_net_change = round((sum(net_change_list) / len(net_change_list)),2)

# Generate the output summary
analysis = (
    f'Financial Analysis\n'
    f'-----------------------------\n'
    f'Total Months: {str(total_months)}\n'
    f'Total: ${total_net:10,.0f}\n'
    f'Average Change: ${average_net_change:10,.2f}\n'
    f'Greatest Increase in Profits: {month_greatest_increase} (${greatest_increase:10,.0f})\n'
    f'Greatest Decrease in Profits: {month_greatest_decrease} (${greatest_decrease:10,.0f})\n'
) 
print(analysis)


# Write the results to a text file

with open(file_to_output, "w") as txt_file:
    txt_file.write(analysis)