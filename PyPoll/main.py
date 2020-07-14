# import csv and open
import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path, newline='')as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    # variables...
    candidate = []
    vote_tally = {}
    
    #loop complete list of candidates who received votes
    for x in reader:
        candidate = x[2]
        if candidate in vote_tally:
            vote_tally[candidate] = vote_tally[candidate]+1
        else:  
            vote_tally[candidate] = 1

    # votes for each candidate
    khan = vote_tally["Khan"]
    correy = vote_tally["Correy"]
    li = vote_tally["Li"]
    otooley = vote_tally["O'Tooley"]

    # calculate total number of votes included in dataset
    total_votes = khan + correy + li + otooley

    # percentages for each candidate
    #(total votes each candidate received divided by vote count)
    khan_percent = (khan/total_votes) * 100
    khan_percent = format(khan_percent, '.3f')

    correy_percent = (correy/total_votes) * 100
    correy_percent = format(correy_percent, '.3f')
    
    li_percent = (li/total_votes) * 100
    li_percent = format(li_percent, '.3f')

    otooley_percent = (otooley/total_votes) * 100
    otooley_percent = format(otooley_percent, '.3f')

# Print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Khan: " + str(khan_percent) + "% " + "(" + str(khan) + ")")
print("Correy: " + str(correy_percent) + "% " + "(" + str(correy) + ")")
print("Li: " + str(li_percent) + "% " + "(" + str(li) + ")")
print("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley) + ")")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")  

# output text file
with open("Analysis/output","w") as textfile:
    textfile.write("Election Results")
    textfile.write("\n")
    textfile.write("------------------------")
    textfile.write("\n")
    textfile.write("Total Votes: " + str(total_votes))
    textfile.write("\n")
    textfile.write("-------------------------")
    textfile.write("\n")
    textfile.write("Khan: " + str(khan_percent) + "% " + "(" + str(khan) + ")")
    textfile.write("\n")
    textfile.write("Correy: " + str(correy_percent) + "% " + "(" + str(correy) + ")")
    textfile.write("\n")
    textfile.write("Li: " + str(li_percent) + "% " + "(" + str(li) + ")")
    textfile.write("\n")
    textfile.write("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley) + ")")
    textfile.write("\n")
    textfile.write("-------------------------")
    textfile.write("\n")
    textfile.write("Winner: Khan")
    textfile.write("\n")
    textfile.write("-------------------------")  
    