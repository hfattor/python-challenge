import os
import csv

vote_total = 0
candidate_list = []
x = 0
vote_count = 0
vote_count_list = []

# Path to collect data from the Resources folder
pypoll_csv = './Resources/election_data.csv'

with open(pypoll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# Loop through the data
    for row in csvreader:
        voter = str(row[0])
        votee = str(row[2])
    

#number of rows/ballot numbers (minus header)

        vote_total += 1

#list unique names in 3rd column
    
        if votee not in candidate_list:
            candidate_list.append(str(votee))

#number of votes for each candidate, divided by total votes, formatted as percentage

    for row in csvreader:
        if votee = str(candidate_list[x]):
            vote_count += 1
        
        else continue
            
        vote_count_list.append(int(vote_count))

        x += 1

#total number of votes each candidate won
    print(f'Election Results')
    print(f'--------------------------')
    print(f'Total votes: {vote_total}')
    print(f'--------------------------')
    for value in candidate_list:
        print(f'{value}:')

    print(f'{vote_count_list}')

#name with most votes




#Export as text file

    print("Done")