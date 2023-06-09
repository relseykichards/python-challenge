import os
import csv
import numpy as np

csvpath = os.path.join('Resources','budget_data.csv')
# creating variables
total_value= 0
total_month= 0
greatest_profit= 0
greatest_loss= 0
greatest_profit_month=""
greatest_loss_month=""
change_of_profit= []

# opening csv fle and skipping header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    previous_value= 0
    if_first_row= True

    for line in csvreader:
        current_value= int(line[1])
        current_month= line[0]
        total_value+= current_value
        total_month+= 1
        current_profit_loss= current_value - previous_value
    # finding greatest increase and decrease in profit
        if current_profit_loss > greatest_profit:
            greatest_profit = current_profit_loss
            greatest_profit_month = current_month 

        if current_profit_loss < greatest_loss:
            greatest_loss = current_profit_loss
            greatest_loss_month = current_month
    # finding average of change of value 
        previous_value = current_value 
        if if_first_row:
            if_first_row = False
            continue
        change_of_profit.append(current_profit_loss)
    average_change_profit= round((sum(change_of_profit))/max(len(change_of_profit),1))

    print(f"Total profit/losses: ${total_value}")
    print(f"Total months: {total_month}")
    print(f"Greatest Increase in profits: {greatest_profit_month} ${greatest_profit}")
    print(f"Greatest Decrease in Profits: {greatest_loss_month} ${greatest_loss}")
    print(f"Average change: ${average_change_profit}")

    report = open("profit_loss_report.txt",'w')

    report.write(f"Total profit/losses: ${total_value} \n")
    report.write(f"Total months: {total_month} \n")
    report.write(f"Greatest Increase in profits: {greatest_profit_month} ${greatest_profit} \n")
    report.write(f"Greatest Decrease in Profits: {greatest_loss_month} ${greatest_loss} \n")
    report.write(f"Average change: ${average_change_profit}")

    report.close()