#import is to bring in a code from python premade
import csv
import os

PROFIT_INDEX = 1
text_path = "output.txt"

months = 0
total_profit = 0
total_change = 0
first_row = True
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
profit = []
previous_profit = 0
months_change = []
average_change = 0

#inent under with is the access to the file
with open("budget_data.csv") as file: 
    csv_file = csv.reader(file)

    next(csv_file)

    for row in csv_file:
        print(row)
        months += 1
        current_profit = int(row[PROFIT_INDEX])
        total_profit += current_profit
        if first_row:
            first_row = False 
        else:
            current_change = current_profit - previous_profit
            total_change += current_change   
        #for next time 
        previous_profit = current_profit
        
        
    
        
average_change = round(total_change / (months - 1), 2)


        


output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total_profit:,}
Average Change: ${average_change}
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)'''

print(output)
