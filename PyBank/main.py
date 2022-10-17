import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r', newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	months = 0
	netprofit = 0
	
	previousprofit = 0
	currentprofit = 0

	totalchange = 0
	change = 0

	greatestIncrease = 0
	greatestDecrease = 0

	for line in csvreader:
		months += 1
		
		netprofit += int(line[1])

		currentprofit = int(line[1])

		if previousprofit != 0:
			change = (currentprofit - previousprofit)
			totalchange += change

		if change >= greatestIncrease:
			greatestIncrease = change

		if change <= greatestDecrease:
			greatestDecrease = change
		
		previousprofit = currentprofit

	
	print('Financial Analysis')
	print('----------------------------')
	print(f'Total Months: {months}')
	print(f'Total: ${netprofit}')
	print(f'Average Change: ${round(totalchange/86, 2)}')
	print(f'Greatest Increase in Profits: ${greatestIncrease}')
	print(f'Greatest Decrease in Profits: ${greatestDecrease}')
