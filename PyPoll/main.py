import os
import csv
# file path to csv file
voteData = os.path.join("..", "Resources", "election_data.csv")
# initialize variables
totalVotesCast = 0
electionVotes = 0
candidate_dict = {}
electionWinner = ""
candidate = ""
percentCandidate = {}
# read in csv file + skip the headers and store them in a variable "header" in case needed
with open(voteData, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header_row = next(csvreader)
    # count total votes and loop through to store the candidates in a dictionary
    for row in csvreader:
        totalVotesCast = totalVotesCast + 1
        candidate = row[2]
        if candidate in candidate_dict:
            candidate_dict[candidate] += 1
        else:
            candidate_dict[candidate] = 1

# calculate election winner and percentages
for candidateName, voteTally in candidate_dict.items():
    if voteTally > electionVotes:
            electionVotes = voteTally
            electionWinner = candidateName

# Print the output to the terminal
candidate_print = ""
for candidate, voteTally in candidate_dict.items():
    candidate_print = f"{candidate_print} {candidate}: ({int(round((voteTally/totalVotesCast)*100, 2))}%) ({voteTally})\n"
voteData = f"""
Election Results
---------------------------------
Total Votes: {totalVotesCast}
---------------------------------
{candidate_print}
---------------------------------
Winner: {electionWinner}
---------------------------------
"""
print(voteData)
#print(candidate_dict)

# output results to file
output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(voteData)
