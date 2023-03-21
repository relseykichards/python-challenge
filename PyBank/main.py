import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    csv_header = next(csvreader)

    val=0
    count=0
    for line in csvreader:
        val=val+int(line[1])
        count=count+1
    print(f"Total months: {count}")
    print(f"total profit/losses: {val}")

# How to access the correct column? moving average? 

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes
  
# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period
