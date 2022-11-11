import os
import csv

#find path
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# open path
with open(csvpath, 'r+') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# skip header row
    next(csvreader)

    date = []
    profit_losses = []

    for row in csvreader:
        date.append(row[0])
        profit_losses.append(int(row[1]))

# print total months
    total_months = len(date)

# total amount
    total_amount = sum(profit_losses)

# average change
    change = []

    for i in range(total_months-1):
        change.append(profit_losses[i+1] - profit_losses[i])
    sum_change = sum(change)
    average_change = round(sum_change/len(change), 2)

# Greatest increase/decrease in profits
    greatest_increase = max(change)
    greatest_decrease = min(change)
    greatest_increase_index = change.index(max(change))
    greatest_increase_date = (date[greatest_increase_index+1])
    greatest_decrease_index = change.index(min(change))
    greatest_decrease_date = (date[greatest_decrease_index+1])

print(
f"""Financial Analysis
----------------------------
Total months: {total_months}
Total: ${total_amount}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})""")