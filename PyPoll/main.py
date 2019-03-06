import os
import csv


# Define path to csv file
election_csv = os.path.join("Resources", "election_data.csv")


# List to append csv row[2], "Candidate"
candidate_list = []


# List to append csv row[0], "Voter ID"
voter_id_list = []


# List to append and only contain "unique" candidates from total list
unique_candidate_list = []


# List to append and only contain vote counts for each of the unique candidates.
# As long, the index position of each count will correspond to the index
# position of each unique candidate in unique_candidate_list
unique_vote_count_list = []


# List to append and only contain percentage of votes for each of the unique candidates
unique_percent_list = []


# Open csv, comma separated, header is present
with open(election_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # For every row in csv file
    for row in csvreader:

        # Add voter ID from csv to newly created and empty total list
        voter_id_list.append(row[0])

        # Add candidates from csv to newly created and empty total list
        candidate_list.append(row[2])


# Determine total number of votes
vote_count = int(len(candidate_list))


# Create unique list of candidates from total list
for v in range(vote_count):
    if candidate_list[int(v)] not in unique_candidate_list:
        unique_candidate_list.append(candidate_list[int(v)])


# Determine how many unique candidates there are
candidate_count = int(len(unique_candidate_list))


# Create a list of unique candidate vote counts for each candidate in unique_candidate_list
for u in range(candidate_count):
    unique_vote_count = 0
    for c in range(vote_count):
        if candidate_list[int(c)] == unique_candidate_list[int(u)]:
            unique_vote_count += 1
    unique_vote_count_list.append(unique_vote_count)


# Calculate and append unique vote percentage for each candidate in unique_candidate_list
for x in range(candidate_count):
    unique_percent = 0
    unique_percent = (unique_vote_count_list[int(x)] / vote_count * 100)
    unique_percent_list.append(unique_percent)


# Determine name of winner
for w in range(candidate_count):
    if max(unique_vote_count_list) == unique_vote_count_list[int(w)]:
        winner = unique_candidate_list[int(w)]


# Print Election Results in terminal
print("")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")
for p in range(candidate_count):
    print(f"{unique_candidate_list[int(p)]}: {round(unique_percent_list[int(p)],3)}% ({unique_vote_count_list[int(p)]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


# Create text file, write Election Results, close
text_file = open("Election Results.txt", "w")
text_file.write("Election Results\n")
text_file.write("----------------------------\n")
text_file.write(f"Total Votes: {vote_count}\n")
text_file.write("----------------------------\n")
for z in range(candidate_count):
    text_file.write(f"{unique_candidate_list[int(z)]}: {round(unique_percent_list[int(z)],3)}% ({unique_vote_count_list[int(z)]})\n")
text_file.write("----------------------------\n")
text_file.write(f"Winner: {winner}\n")
text_file.write("----------------------------\n")
text_file.close()


# Print confirmation of completion in terminal
print("")
print("Process complete")