import os
import csv


# Define path to csv file
election_csv = os.path.join("Resources", "election_data.csv")


# List to append csv row[2], "Candidate"
candidate_list = []


# List to append and contain only "unique" candidates from total list
unique_candidate_list = []


cand_one = 0
cand_two = 0
cand_thr = 0
cand_fou = 0


# Open csv, comma separated, header is present
with open(election_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # For every row in csv file
    for row in csvreader:

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


# TODO: need to write code that says, for 0 to 3.5 mil, if candidate in candidate list equals
# candidate in unique candidate list, fro 0 to len(candidate count), append the voter id to a list,
# get the len of that list, and place this number in the same index as the unique candidate in a
# new list called candidate_votes_list
# Then, this won't be specific to how many candidates are on the list - and if it changes, it will be
# flexible and calculate for any number of candidates on the list.  Then to call these total counts of voters,
# we can just use the parameter of the unique candidate index to iterate the candidate_votes_list
# and return the total number


# TODO:
for c in range(vote_count):
    if candidate_list[int(c)] == unique_candidate_list[0]:
        cand_one += 1
    elif candidate_list[int(c)] == unique_candidate_list[1]:
        cand_two += 1
    elif candidate_list[int(c)] == unique_candidate_list[2]:
        cand_thr += 1
    else:
        cand_fou += 1


can_one_per = cand_one / vote_count * 100
can_two_per = cand_two / vote_count * 100
can_thr_per = cand_thr / vote_count * 100
can_fou_per = cand_fou / vote_count * 100


largest = [can_one_per, can_two_per, can_thr_per, can_fou_per]


for w in range(candidate_count):
    if max(largest) == largest[w]:
        winner = unique_candidate_list[w]


# Print Election Results in terminal
print("")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")
print(f"{unique_candidate_list[0]}: {round(can_one_per,3)}% ({cand_one})")
print(f"{unique_candidate_list[1]}: {round(can_two_per,3)}% ({cand_two})")
print(f"{unique_candidate_list[2]}: {round(can_thr_per,3)}% ({cand_thr})")
print(f"{unique_candidate_list[3]}: {round(can_fou_per,3)}% ({cand_fou})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


# Create text file, write Election Results, close
text_file = open("Election Results.txt", "w")
text_file.write("Election Results\n")
text_file.write("----------------------------\n")
text_file.write(f"Total Votes: {vote_count}\n")
text_file.write("----------------------------\n")
text_file.write(f"{unique_candidate_list[0]}: {round(can_one_per,3)}% ({cand_one})\n")
text_file.write(f"{unique_candidate_list[1]}: {round(can_two_per,3)}% ({cand_two})\n")
text_file.write(f"{unique_candidate_list[2]}: {round(can_thr_per,3)}% ({cand_thr})\n")
text_file.write(f"{unique_candidate_list[3]}: {round(can_fou_per,3)}% ({cand_fou})\n")
text_file.write("----------------------------\n")
text_file.write(f"Winner: {winner}\n")
text_file.write("----------------------------\n")
text_file.close()


# Print confirmation of completion in terminal
print("")
print("Process complete")