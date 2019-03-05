import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

dates_list = []
tot_prof_list = []
chg_list = []

summed = 0
mth_chg = 0
gr_inc = 0
gr_dec = 0
inc_month = "Month"
dec_month = "Month"


# with open(budget_csv, newline="", encoding='utf-8') as csvfile:
with open(budget_csv, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        
        # Add dates to list
        dates_list.append(row[0])

        # Add profit/loss to list
        tot_prof_list.append(int(row[1]))

# Get count of dates
months_total = int(len(dates_list))


# *********GATHER ALL FOR LOOPS HERE*********
# Sum total profit/loss in list
for prof_loss in tot_prof_list:
    summed += prof_loss


# ------------------------------------------------
# Calculate change per month & add to list
for i in range(months_total-1):
    chg_list.append(tot_prof_list[int(i+1)] - tot_prof_list[int(i)])

# Sum month-to-month changes from list
for chg in chg_list:
    mth_chg += chg


# ------------------------------------------------
# Calculate greatest monthly increase
for g in range(months_total-1):
    if chg_list[int(g)] > gr_inc:
        gr_inc = chg_list[int(g)]
        inc_month = dates_list[int(g+1)]

# ------------------------------------------------
# Calculate greatest monthly decrease
for z in range(months_total-1):
    if chg_list[int(z)] < gr_dec:
        gr_dec = chg_list[int(z)]
        dec_month = dates_list[int(z+1)]




# *********GATHER ALL VARIABLE CREATION HERE*********


# Create variable for average monthly change
avg_chg = mth_chg / (months_total-1)


print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months_total}")
print(f"Total: ${summed}")
print(f"Average Change: ${round(avg_chg,2)}")
print(f"Greatest Increase in Profits: {inc_month} $({gr_inc})")
print(f"Greatest Decrease in Profits: {dec_month} $({gr_dec})")


text_file = open("Financial Analysis.txt", "w")
text_file.write(f"Financial Analysis\n")
text_file.write("----------------------------\n")
text_file.write(f"Total Months: {months_total}\n")
text_file.write(f"Total: ${summed}\n")
text_file.write(f"Average Change: ${round(avg_chg,2)}\n")
text_file.write(f"Greatest Increase in Profits: {inc_month} $({gr_inc})\n")
text_file.write(f"Greatest Decrease in Profits: {dec_month} $({gr_dec})")
text_file.close()

print("")
print("Process complete")
