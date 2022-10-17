import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	profit = next(csvreader)

	months = 0
	
	for line in csvreader:
		months += 1
		profit += line[1]
	
	print('Financial Analysis')
	print('----------------------------')
	print(f'Total Months: {months}')

	print(f'Total: ${profit}')

	print(f'Average Change: ')

	print(f'Greatest Increase in Profits: ')

	print(f'Greatest Decrease in Profits:')