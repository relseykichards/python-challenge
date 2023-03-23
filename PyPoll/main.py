import os
import csv
import numpy as np

csvpath = os.path.join('Resources','election_data.csv')
# creating variables
vote_count = 0
candidates = []
total_votes = 0
charles_count=0
diana_count=0
raymon_count=0
winner=""
# accessing csv file and skipping header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
   
    for line in csvreader:
        vote_count = vote_count+1
        total_votes+=vote_count

        # adding candidates to list:
        if line[2] not in candidates:
            candidates.append(line[2])

        # adding each vote per each candidate:
        if line[2] == "Charles Casper Stockham":
            charles_count = charles_count + 1

        if line[2] == "Diana DeGette":
            diana_count = diana_count + 1
        
        if line[2] == "Raymon Anthony Doane":
            raymon_count = raymon_count + 1

#dividing each candidates vote count by the total and 
# formatting percentages to a whole number
        charles_percent = charles_count/vote_count
        charles_percent_formatted = round(charles_percent * 100)

        diana_percent = diana_count/vote_count
        diana_percent_formatted = round(diana_percent * 100)

        raymon_percent = raymon_count/vote_count
        raymon_percent_formatted = round(raymon_percent * 100)

#to find winner
        if charles_count > diana_count and charles_count > raymon_count:
            winner = "Charles Casper Stockham"
        if diana_count > charles_count and diana_count > raymon_count:
            winner = "Diana DeGette"
        if raymon_count > charles_count and raymon_count > diana_count:
            winner = "Raymond Anthony Doane"

    
    

    print(f"Total votes: {vote_count}")        
    print(f"{candidates[0]}: {charles_count} votes, {charles_percent_formatted}%")
    print(f"{candidates[1]}: {diana_count} votes, {diana_percent_formatted}%")
    print(f"{candidates[2]}: {raymon_count} votes, {raymon_percent_formatted}%") 
    print(f"The winner is: {winner}")  

    report = open("Analysis/poll_report.txt",'w')

    report.write(f"Total votes: {vote_count} \n")        
    report.write(f"{candidates[0]}: {charles_count} votes, {charles_percent_formatted}% \n")
    report.write(f"{candidates[1]}: {diana_count} votes, {diana_percent_formatted}% \n")
    report.write(f"{candidates[2]}: {raymon_count} votes, {raymon_percent_formatted}% \n") 
    report.write(f"The winner is: {winner}") 

    report.close()

  
 
