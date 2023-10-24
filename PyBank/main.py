import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# make a text file for results
output_file_path = os.path.join('analysis', 'budget_data_results.txt')

# list and define all variables
total_months = 0
total_profits = 0
prior_profits = None
total_change = 0
change_count = 0
max_increase = 0
max_increase_date = None
max_decrease = 0
max_decrease_date = None

with open(output_file_path, 'w') as output_file:
# Open the file and read it line by line
    with open(csvpath, 'r') as file:
        file.readline()
    
        for line in file:
            # count total months
            total_months += 1
            # calculate total profits
            parts = line.strip().split(',')
            date = parts[0]
            profits = int(parts[1])
            total_profits += profits

            if prior_profits is not None:
                change = profits - prior_profits
                total_change += change
                change_count += 1
                if change > max_increase:
                    max_increase = change
                    max_increase_date = date
                elif change < max_decrease:
                    max_decrease = change
                    max_decrease_date = date

            prior_profits = profits

    # find average change 
    average_change = total_change / change_count

    output_file.write("Financial Analysis\n")
    output_file.write("-------------------\n")
    output_file.write(f"Total: ${total_profits}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

print("Financial Analysis")
print("---------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")
