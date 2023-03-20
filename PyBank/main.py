import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    csv_header = next(csvreader)
# MONTH COUNT
    month_count = sum(1 for row in csvreader)
    print(month_count)

    for row in csvreader: 
       print(row)

def  net_total_sum():
    net_total= 0
    # reader=csv.reader
    # for line in reader:
    net_total+=int(row[1])
    return net_total
        
print(net_total_sum())



