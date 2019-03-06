# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`

import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

vote_id_list = []
cand_list = []
uniq_cand_list = []
cand_one = 0
cand_two = 0
cand_thr = 0
cand_fou = 0

# with open(election_csv, newline="", encoding='utf-8') as csvfile:
with open(election_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        
        # Add voter id to list
        vote_id_list.append(row[0])

        # Add candidates to list
        cand_list.append(row[2])


# Get count of votes
vote_count = int(len(vote_id_list))

# Get unique list of candidates from total list
for i in range(vote_count):
    if cand_list[int(i)] not in uniq_cand_list:
        uniq_cand_list.append(cand_list[int(i)])


# Get length of unique list
uniq_lenth = int(len(uniq_cand_list))


for j in range(vote_count):
    if cand_list[int(j)] == uniq_cand_list[0]:
        cand_one += 1
    elif cand_list[int(j)] == uniq_cand_list[1]:
        cand_two += 1
    elif cand_list[int(j)] == uniq_cand_list[2]:
        cand_thr += 1
    else:
        cand_fou += 1

can_one_per = cand_one / vote_count * 100
can_two_per = cand_two / vote_count * 100
can_thr_per = cand_thr / vote_count * 100
can_fou_per = cand_fou / vote_count * 100


# index of largest in list
largest_list = [can_one_per, can_two_per, can_thr_per, can_fou_per]


print("")
print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")
print(f"{uniq_cand_list[0]}: {round(can_one_per,3)}% ({cand_one})")
print(f"{uniq_cand_list[1]}: {round(can_two_per,3)}% ({cand_two})")
print(f"{uniq_cand_list[2]}: {round(can_thr_per,3)}% ({cand_thr})")
print(f"{uniq_cand_list[3]}: {round(can_fou_per,3)}% ({cand_fou})")
print("----------------------------")
print(f"Winner: {uniq_cand_list[0]}")
print("----------------------------")