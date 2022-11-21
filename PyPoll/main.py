import os
import csv

#find path
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# open path
with open(csvpath, 'r+') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# skip header row
    next(csvreader)

    ballotID = []
    candidates = []
    candidate_list = []

    for row in csvreader:
        ballotID.append(row[0])
        candidates.append(str(row[2]))

# total votes
    total_votes = len(ballotID)
    print(total_votes)

# total list of candidates
    for i in candidates:
        if i not in candidate_list:
            candidate_list.append(i)
    
    print(candidate_list)

# percent
    candidate_votes = {}
    percentage = []
    for name in candidates:
        if name not in candidate_votes:
            candidate_votes[name]= 1
        else: 
            candidate_votes[name] += 1
    
    print(candidate_votes)

    def find_percentage(candidate_votes, name, total_ballots):
        return round(candidate_votes[name]/total_ballots * 100,3)

    for name in candidate_votes:
        percentage.append(find_percentage(candidate_votes, name, total_votes))
    
    print_names = list(candidate_votes.keys())
    print_votes = list(candidate_votes.values())

    print(f"""
Election Results
---------------------------
Total Votes: {total_votes}
---------------------------
{print_names[0]}: {percentage[0]}% ({print_votes[0]})
{print_names[1]}: {percentage[1]}% ({print_votes[1]})
{print_names[2]}: {percentage[2]}% ({print_votes[2]})
----------------------------
Winner: {max(candidate_votes, key=candidate_votes.get)}
----------------------------""")

# Export a text file with the results.
output_path = os.path.join('PyPoll','analysis','budget_data_analysis.txt')
output = open(output_path, "w")
output.write(
f"""
Election Results
---------------------------
Total Votes: {total_votes}
---------------------------
{print_names[0]}: {percentage[0]}% ({print_votes[0]})
{print_names[1]}: {percentage[1]}% ({print_votes[1]})
{print_names[2]}: {percentage[2]}% ({print_votes[2]})
----------------------------
Winner: {max(candidate_votes, key=candidate_votes.get)}
----------------------------""")
output.close()