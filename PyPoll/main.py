import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# make a text file for results
txt_path = os.path.join('analysis', 'election_data_results.txt')

# dictionary
candidates = {}

#variables
total_votes = 0
winner = ""
winner_votes = 0

with open(txt_path, 'w') as txt_file:
    with open(csvpath, 'r') as file:
        file.readline()

        for row in file:
            #add candidates
            candidate_name = row[2]

            total_votes += 1
            
            if candidate_name in candidates:
                candidates[candidate_name] += 1
            else: 
                candidates[candidate_name] = 1

#find winner
for winner_name, votes in candidates.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = winner_name
    


# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage_votes = (votes / total_votes) * 100
    print(f"{candidate}: {percentage_votes:.1f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

txt_file.write("Election Results\n")
txt_file.write("-------------------\n")
txt_file.write(f"Total Votes: {total_votes}\n")
txt_file.write("-------------------\n")
for candidate, votes in candidates.items():
    percentage_votes = (votes / total_votes) * 100
    txt_file.write(f"{candidate}: {percentage:.1f}% ({votes})\n")
txt_file.write("-------------------\n")
txt_file.write(f"Winner: {winner}\n")
txt_file.write("-------------------\n")
