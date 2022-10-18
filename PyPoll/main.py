import os
import csv

# reads the csv file election_data and gets the results from the data 
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r', newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	# initialize variables
	totalVotes = 0
	candidate1_votes = 0
	candidate2_votes = 0
	candidate3_votes = 0
	winning_candidate = ''

	# tallies the votes for the candidates
	for line in csvreader:
		totalVotes += 1

		if str(line[2]) == "Charles Casper Stockham":
			candidate1_votes += 1
		
		if str(line[2]) == "Diana DeGette":
			candidate2_votes += 1

		if str(line[2]) == "Raymon Anthony Doane":
			candidate3_votes += 1

	# determines the winner of the election based on which candidate has the most votes
	if candidate1_votes > candidate2_votes and candidate1_votes > candidate3_votes:
		winning_candidate = "Charles Casper Stockham"
	elif candidate2_votes > candidate1_votes and candidate2_votes > candidate3_votes:
		winning_candidate = "Diana DeGette"
	else:
		winning_candidate = "Raymon Anthony Doane"

	# prints out the election results to the terminal
	print('Election Results')
	print('-------------------------')
	print(f'Total Votes: {totalVotes}')
	print('-------------------------')
	print(f'Charles Casper Stockham: {round((candidate1_votes/totalVotes)*100, 3)}% ({candidate1_votes})')
	print(f'Diana DeGette: {round((candidate2_votes/totalVotes)*100, 3)}% ({candidate2_votes})')
	print(f'Raymon Anthony Doane: {round((candidate3_votes/totalVotes)*100, 3)}% ({candidate3_votes})')
	print('-------------------------')
	print(f'Winner: {winning_candidate}')
	print('-------------------------')

# writes the election results to a txt file
output_path = os.path.join("Analysis", "Module 3 PyPoll Analysis.txt")

with open(output_path, 'w') as file:
	file.write('Election Results' + '\n')
	file.write('-------------------------\n')
	file.write(f'Total Votes: {totalVotes}\n')
	file.write('-------------------------' + '\n')
	file.write(f'Charles Casper Stockham: {round((candidate1_votes/totalVotes)*100, 3)}% ({candidate1_votes})\n')
	file.write(f'Diana DeGette: {round((candidate2_votes/totalVotes)*100, 3)}% ({candidate2_votes})\n')
	file.write(f'Raymon Anthony Doane: {round((candidate3_votes/totalVotes)*100, 3)}% ({candidate3_votes})\n')
	file.write('-------------------------' + '\n')
	file.write(f'Winner: {winning_candidate}\n')
	file.write('-------------------------' + '\n')
