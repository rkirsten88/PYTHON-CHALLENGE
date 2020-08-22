import os
import csv

#set path
Election_CSV = os.path.join('.', 'Resources', 'election_data.csv')

#Variables
Total_Votes = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0

#open csv file
with open(Election_CSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
#skip header
    csv_header = next(csvfile)
 #read csv file   
    for row in csvreader:
#count total votes
        Total_Votes += 1
#if name is found, add 1. if not, go to next name, else last name. 
        if (row[2] == "Khan"):
            Khan += 1
        elif (row[2] == "Correy"):
            Correy += 1
        elif (row[2] == "Li"):
            Li += 1
        else:
            OTooley += 1
    #percent calculations with new name_percent variable
    Khan_percent = Khan/Total_Votes
    Correy_percent = Correy/Total_Votes
    Li_percent = Li/Total_Votes
    OTooley_percent = OTooley/Total_Votes
    #determine winner with max() from each vote count
    winner = max(Khan, Correy, Li, OTooley)
    #new if statement to determine which "winning_name" is the one to print
    if winner == Khan:
        winning_name = "Khan"
    elif winner == Correy:
        winning_name = "Correy"
    elif winner == Li:
        winning_name = "Li"
    else:
        winning_name = "OTooley"

#print results (with 3 decimals per instructions)
print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {Total_Votes}")
print(f"--------------------------------")
print(f"Khan: {Khan_percent:.3%} ({Khan})")
print(f"Correy: {Correy_percent:.3%} ({Correy})")
print(f"Li: {Li_percent:.3%} ({Li})")
print(f"O'Tooley: {OTooley_percent:.3%} ({OTooley})")
print(f"--------------------------------")
print(f"Winner: {winning_name}")
print(f"Fanfare: CONGRATS TO {winning_name}! Hip Hip, Hooray!")
print(f"--------------------------------")



#output file
dump_file = os.path.join(".", "Analysis", "PollResults.text")

#open file and write the new jawn with \n to go to next line in txtfile
with open(dump_file, 'w',) as txtfile:

    txtfile.write(f"Election Results\n")
    txtfile.write(f"--------------------------------\n")
    txtfile.write(f"Total Votes: {Total_Votes}\n")
    txtfile.write(f"--------------------------------\n")
    txtfile.write(f"Khan: {Khan_percent: .3%} ({Khan})\n")
    txtfile.write(f"Correy: {Correy_percent:.3%} ({Correy})\n")
    txtfile.write(f"Li: {Li_percent:.3%} ({Li})\n")
    txtfile.write(f"O'Tooley: {OTooley_percent:.3%} ({OTooley})\n")
    txtfile.write(f"--------------------------------\n")
    txtfile.write(f"Winner: {winning_name}\n")
    txtfile.write(f"--------------------------------\n")

