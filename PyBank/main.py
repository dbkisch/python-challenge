# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
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

    # Track the total and net change
    total_net = int(firstrow[1])
    total_months = 1
    last_profit = int(firstrow[1])
 
    # Process each row of data
    for row in reader:
        month = str(row[0])
        profit = int(row[1])
        
        # Track the total
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

# Calculate the average net change across the months using a defined function
#def average(numbers):
#    length = len(numbers)
#    total = 0.0
#    for number in numbers:
#        total += number
#    return round((total / length),2)

#average(net_change_list)

# Calculate the average net change across the months using built-in functions
average_net_change = round((sum(net_change_list) / len(net_change_list)),2)

# Generate the output summary
print("")
print("Financial Analysis")
print("")
print("-----------------------------")
print("")
print(f'Total Months: {str(total_months)}')
print("")
print(f'Total: ${str(total_net)}')
print("")
print(f'Average Change: ${str(average_net_change)}')
print("")
print(f'Greatest Increase in Profits: {month_greatest_increase} (${str(greatest_increase)})')
print("")
print(f'Greatest Decrease in Profits: {month_greatest_decrease} (${str(greatest_decrease)})')
print("")
# Print the output



# Write the results to a text file

with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("")
    txt_file.write("-----------------------------")
    txt_file.write("")
    txt_file.write(f'Total Months: {str(total_months)}')
    txt_file.write("")
    txt_file.write(f'Total: ${str(total_net)}')
    txt_file.write("")
    txt_file.write(f'Average Change: ${str(average_net_change)}')
    txt_file.write("")
    txt_file.write(f'Greatest Increase in Profits: {month_greatest_increase} (${str(greatest_increase)})')
    txt_file.write("")
    txt_file.write(f'Greatest Decrease in Profits: {month_greatest_decrease} (${str(greatest_decrease)})')
    txt_file.write("")