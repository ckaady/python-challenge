# import csv and open
import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path, newline='')as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)

    # calculate total number of months included in dataset
    # variables/lists ... loop
    month_count = []
    revenue = []
    diff_revenue = []

    for row in reader:
        month_count.append(row[0])
        revenue.append(int(row[1]))
    for i in range(len(revenue)-1):
        diff_revenue.append(revenue[i+1]-revenue[i])
        
# calculate net total "profit/losses" 
# average of changes in "profits/losses" 
# greatest increase in profits (date and amount) and greatest decrease in losses (date and amount) - LOOP
increase = max(diff_revenue)
decrease = min(diff_revenue)

# using data from indexes... 
month_increase = diff_revenue.index(max(diff_revenue))+1
month_decrease = diff_revenue.index(min(diff_revenue))+1

#print info 
print("Financial Analysis")
print("---------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(revenue)}")
print(f"Average Change: {round(sum(diff_revenue)/len(diff_revenue),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

# analysis output text file
## print the analysis to the terminal and export a text file with the results
#find path to create text file within analysis folder
#output = output.txt
with open("Analysis/output","w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n")
    textfile.write("------------------------")
    textfile.write("\n")
    textfile.write(f"Total Months:{len(month_count)}")
    textfile.write("\n")
    textfile.write(f"Total: ${sum(revenue)}")
    textfile.write("\n")
    textfile.write(f"Average Change: $ {round(sum(diff_revenue)/len(diff_revenue),2)}")
    textfile.write("\n")
    textfile.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    textfile.write("\n")
    textfile.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))}")
    
    