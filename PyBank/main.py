import os
import csv


pl_current = 0
pl_change = 0
pl_change_total = 0
pl_average = 0
month_total = 0
pl_pos_change = 0
pl_neg_change = 0
holder = 0
pl_total = 0
holder2 = 0

# Path to collect data from the Resources folder
pybank_csv = './Resources/budget_data.csv'

with open(pybank_csv, 'r') as csvfile:

# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# Loop through the data
    for row in csvreader:
        date = str(row[0])
        pl = float(row[1])

#Find total months
        month_total += 1
    
#Profit/Loss total
        pl_total += int(pl)

#Profit/Loss average over time
        pl_current = float(pl)

        if holder != 0:
            pl_change = float(pl_current) - float(holder)
            pl_change_total += float(pl_change)
            
        holder = float(pl_current)
    
#Profit/Loss high and low calculation
        pl_current = float(pl)

        if holder2 != 0:
            pl_change = float(pl_current) - float(holder2)
                
            if pl_pos_change <= pl_change:
                pl_pos_change = pl_change
                date_current_pos = date
                
            elif pl_neg_change >= pl_change:
                pl_neg_change = pl_change
                date_current_neg = date
            
        holder2 = float(pl_current)
    
    pl_average = round(float(pl_change_total) / int(month_total), 2) 

    print(f'Financial Analysis')
    print(f'--------------------------')
    print(f'Total months: {month_total}')
    print(f'Total profit/loss: ${pl_total}')
    print(f'Average profit/loss change: ${pl_average}')
    print(f'Greatest Increase in profits: {date_current_pos} ${pl_pos_change}')
    print(f'Greatest Loss in profits: {date_current_neg} ${pl_neg_change}')


#Export as text file

# Set variable for output file
output_file = os.path.join("pybank_final.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis \n")
    datafile.write("-------------------------- \n")
    datafile.write(f'Total months: {month_total} \n')
    datafile.write(f'Total profit/loss: ${pl_total} \n')
    datafile.write(f'Average profit/loss change: ${pl_average} \n')
    datafile.write(f'Greatest Increase in profits: {date_current_pos} (${pl_pos_change}) \n')
    datafile.write(f'Greatest Loss in profits: {date_current_neg} (${pl_neg_change}) \n')
    datafile.close

