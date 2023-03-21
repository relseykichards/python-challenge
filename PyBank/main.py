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
    print(f"The total number of months in this period are: {val}")
    print(f"The total profit/losses during this period is: {count}")


