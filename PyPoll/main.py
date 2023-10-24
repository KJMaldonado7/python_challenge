import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# make a text file for results
output_file_path = os.path.join('analysis', 'election_data_results.txt')

# list
candidates = []

#variables
total_votes = 0
winner = ""
winner_votes = 0

with open(output_file_path, 'w') as output_file:
    with open(csvpath, 'r') as file:
        file.readline()

        for row in file:
            #add candidates
            candidates.append(row[2])

            total_votes += 1
            percent = round(int(row[0]) / total_votes * 100, 2)
    
    output_file.write("Election Results\n")
    output_file.write("-------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------\n")
        for candidate in results.values():
             output_file.write(f"{candidate['name']}: {candidate['percentage']:.1f}% ({candidate['votes']})\n")
    output_file.write("-------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------\n")

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in results.values():
    print(f"{candidate['name']}: {candidate['percentage']:.1f}% ({candidate['votes']})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")