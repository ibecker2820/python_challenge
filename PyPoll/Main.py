

import os
import csv

#Variables for counting the vote.
candidates = []
number_of_votes = 0
vote_counts = []

election_csv = os.path.join('Resources','election_data.csv')

with open(election_csv) as electionfile:
    csvreader = csv.reader(electionfile)

    #Gets rid of the header for the analysis
    csvheader = next(csvreader)
    
    for row in csvreader:
        #Keep track of the number of votes.
        number_of_votes = number_of_votes + 1
        #Check the candidate voted for.
        candidate = row[2]
        #Count votes if the candidate has votes otherwise make a new candidate
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)

#Variables for analysis.
percentage = []
max_votes = vote_counts[0]
max_index = 0

for person in range(len(candidates)):
    vote_percentage = round(vote_counts[person]/number_of_votes*100, 2)
    percentage.append(vote_percentage)

    if vote_counts[person] > max_votes:
        max_votes = vote_counts[person]
        max_index = person

election_winner = candidates[max_index]

print("Election Results")
print("-----------------------")
print("Total Votes: " + str(number_of_votes))
print("-----------------------")
for persons in range(len(candidates)):
    print(f'{candidates[persons]} : {percentage[persons]}% ({vote_counts[persons]})')
print("-----------------------")
print("Election winner: " + election_winner.upper())  

with open ('Analysis/Election_Analysis.txt','w') as text:
    text.write("Election Results" +"\n")
    text.write("------------------------\n")
    text.write("Total votes: " + str(number_of_votes) + "\n")
    text.write("-----------------------" + "\n")
    for persons in range(len(candidates)):
        text.write(f'{candidates[persons]} : {percentage[persons]}% ({vote_counts[persons]})'+ "\n")
    text.write("-----------------------" + "\n")
    text.write("Election winner: " + election_winner.upper()+ "\n")  

