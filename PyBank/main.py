import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r', newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)
	#print(f"CSV Header: {csv_header}")

	months = 0
	#total = float

	#def print_profits(budget_data):
	#	total = float(budget_data[1])

	#	for line in csvreader:
	#		total += float(budget_data[1])

	for line in csvreader:
	 	months += 1

	print('Financial Analysis')
	print('----------------------------')
	print(f'Total Months: {months}')

	print(f'Total: $')

	print(f'Average Change: ')

	print(f'Greatest Increase in Profits: ')

	print(f'Greatest Decrease in Profits:')
