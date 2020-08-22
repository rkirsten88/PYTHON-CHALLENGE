import os
import csv

# Set path to PyBank -> Resources folder -> budget_data.csv
Budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Set variables for month count and change monthly [Need new empty lists] 
month_count = []
change_monthly = []

#Set variables to zero to start: total number months, net total profit/losses, greatest profit increase amount and date, greatest loss decrease amount and date
total_months = 0
net_total = 0
greatest_profit_increase = 0
greatest_profit_increase_month = 0
greatest_loss_decrease = 0
greatest_loss_decrease_month = 0

# with open() as csvfile: to open and read the budget_data
with open(Budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # header row: ASK ABOUT THIS.
    csv_header = next(csvreader)
    row = next(csvreader)
    
    #set variables for rows
    total_months += 1
    net_total += int(row[1])
    previous_row = int(row[1])

    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

# calculate total number of months, profit/loss net 

    for row in csvreader:

        #calculate total months : total_months = total months + 1 
        total_months += 1
        #net profit/loss over period 
        net_total += int(row[1])

        #calculate change from month to month
        change_total = int(row[1]) - previous_row
        change_monthly.append(change_total)
        previous_row = int(row[1])
        month_count.append(row[0])

        #greatest increase
        if int(row[1]) > greatest_profit_increase:
            greatest_profit_increase = int(row[1])
            greatest_profit_increase_month = row[0]

        #greatest decrease
        if int(row[1]) < greatest_loss_decrease:
            greatest_loss = int(row[1])
            greatest_loss_month = row[0]  
        
    #average change and date (sum/len)
    average_change = sum(change_monthly)/ len(change_monthly)
    #set max change and min change
    highest_profit = max(change_monthly)
    lowest_loss = min(change_monthly)

#print statements of results with f strings
print(f"Financial Analysis")
print(f"--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f} per (some unit of time. month in this case?)")
print(f"Greatest Increase in Profits: {greatest_profit_increase_month}, (${highest_profit})")
print(f"Greatest Loss (Decrease in Profits): {greatest_loss_month}, (${lowest_loss})")

#output file
dump_file = os.path.join(".", "Analysis", "BankingAnalysis.text")

#open file and write the new jawn with \n to go to next line in txtfile
with open(dump_file, 'w',) as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"--------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_profit_increase_month}, (${highest_profit})\n")
    txtfile.write(f"Greatest Loss (Decrease in Profits): {greatest_loss_month}, (${lowest_loss})\n")

