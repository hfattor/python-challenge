import os
import csv

# Path to collect data from the Resources folder
pybank_csv = './Resources/budget_data.csv'

    def financial_analysis(pl_data):
        date = str(pl_data[0])
        pl = float(pl_data[1])
        pl_current = 0
        pl_change = 0
        pl_change_total = 0
        pl_average = 0
        month_total = 0
        pl_pos_change = 0
        pl_neg_change = 0
        holder = 0

        #Find total months
        for date in pl_data:
            month_total += 1

        #Profit/Loss total
        for pl in pl_data:
            pl_total += pl

        #Profit/Loss average over time
        for pl in pl_data:
            pl_current = pl

            if holder != 0:
                pl_change = pl_current - holder
                pl_change_total += pl_change
            
            holder = pl_current
            pl_average == pl_change_total / month_total
        
        #Profit/Loss high and low calculation
        for pl in pl_data:
            pl_current = pl

            if holder != 0:
                pl_change = pl_current - holder
                
                if pl_pos_change <= pl_change:
                    pl_pos_change = pl_change
                
                elif pl_neg_change >= pl_change:
                    pl_neg_change = pl_change
            
            holder = pl_current

        print(f'Total months: {month_total}')
        print(f'Total profit/loss: {pl_total}')
        print(f'Average profit/loss change: {pl_average}')
        print(f'Greatest Increase in profits: {pl_pos_change}')
        print(f'Greatest Loss in profits: {pl_neg_change}')


with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Run function
    financial_analysis(csvreader)

    print("Done")





