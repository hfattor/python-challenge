import os
import csv

vote_total = 0
candidate_list = {}
x = 0
vote_count = 0
winner = ""
votemax = 0

# Path to collect data from the Resources folder
pypoll_csv = os.path.join("Resources", "election_data.csv")

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

#list of candidate names, number of votes they received
        if votee not in candidate_list:
            candidate_list[votee] = 0

        candidate_list[votee] += 1

#Candidate with most votes
    for votee, value in candidate_list.items():
        if value > votemax:
            winner = votee
            votemax = value

#print to terminal
    print(f'Election Results')
    print(f'--------------------------')
    print(f'Total votes: {vote_total}')
    print(f'--------------------------')
    for votee, value in candidate_list.items():
        print(f'{votee}: {round((value/vote_total) *100, 3)}% ({value})')
    print(f'--------------------------')
    print(f'Winner: {winner}')

#easy way to find winner with most votes:
#   print(f'Winner: {max(candidate_list, key=candidate_list.get)}')


#Export as text file

#Set variable for output file
output_file = os.path.join("Analysis", "pypoll_final.txt")

#Open the output file, write above, close file
with open(output_file, "w") as datafile:
    datafile.write("Election Results \n")
    datafile.write("-------------------------- \n")
    datafile.write(f'Total votes: {vote_total} \n')
    datafile.write("-------------------------- \n")
    for votee, value in candidate_list.items():
        datafile.write(f'{votee}: {round((value/vote_total) *100, 3)}% ({value}) \n')
    datafile.write("-------------------------- \n")
    datafile.write(f'Winner: {winner} \n')
    datafile.close
