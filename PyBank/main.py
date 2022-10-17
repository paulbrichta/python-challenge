import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r', newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	months = 0
	netprofit = 0
	totalchange = 0
	averageChange = 0
	changecounter = 0
	greatestIncrease = 0
	greatestDecrease = 0
	
	previousprofit = 0

	for line in csvreader:
		months += 1
		netprofit += int(line[1])

		currentprofit = int(line[1])

		if previousprofit != 0:
			change = currentprofit - previousprofit
			totalchange += change
			changecounter += 1
			greatestIncrease = currentprofit
		previousprofit = currentprofit
	
	print('Financial Analysis')
	print('----------------------------')
	print(f'Total Months: {months}')

	print(f'Total: ${totalchange}')

	print(f'Average Change: ${totalchange}')

	print(f'Greatest Increase in Profits: ${greatestIncrease}')

	print(f'Greatest Decrease in Profits: ${greatestDecrease}')