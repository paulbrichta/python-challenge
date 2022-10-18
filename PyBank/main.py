import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r', newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	months = 0
	netProfit = 0
	
	previousProfit = 0
	currentProfit = 0

	change = 0
	totalChange = 0

	greatestIncrease = 0
	greatestDecrease = 0

	for line in csvreader:
		months += 1
		
		netProfit += int(line[1])

		currentProfit = int(line[1])

		if previousProfit != 0:
			change = (currentProfit - previousProfit)
			totalChange += change

		if change >= greatestIncrease:
			greatestIncrease = change

		if change <= greatestDecrease:
			greatestDecrease = change
		
		previousProfit = currentProfit

	print('Financial Analysis')
	print('----------------------------')
	print(f'Total Months: {months}')
	print(f'Total: ${netProfit}')
	print(f'Average Change: ${round(totalChange/(months-1), 2)}')
	print(f'Greatest Increase in Profits: (${greatestIncrease})')
	print(f'Greatest Decrease in Profits: (${greatestDecrease})')

output_path = os.path.join("Analysis", "Module 3 PyBank Analysis.txt")

with open(output_path, 'w') as file:
	file.write('Financial Analysis' + '\n')
	file.write('----------------------------' + '\n')
	file.write(f'Total Months: {months}\n')
	file.write(f'Total: ${netProfit}\n')
	file.write(f'Average Change: ${round(totalChange/(months-1), 2)}' + '\n')
	file.write(f'Greatest Increase in Profits: (${greatestIncrease})\n')
	file.write(f'Greatest Decrease in Profits: (${greatestDecrease})')
