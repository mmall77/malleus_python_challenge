import os
import csv

# file path to csv file
company_data = os.path.join("..", "Resources", "budget_data.csv")

# data function deprecated
#def companyInfo(company_data):

## list out the names of all variables for calculations
## set variables = 0 to initialize
totalMonths = 0
totalProfit = 0
avgChange = 0
greatestIncrease = 0
greatestDecrease = 0
highestMonth = ""
lowestMonth = ""
change = 0
previousprofloss = 0
changes = []

# read in csv file + skip the headers and store them in a variable "header" in case needed
with open(company_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # for loop to iterate through each row of the cols in the csv file totalProfit iterates
    # through column index 1 to count the profit/losses and adds 1 to the totalMonths in col
    #index 0 as it does so.
    for row in csvreader:
        date = row[0]
        profloss = int(row[1])
        totalProfit += profloss
        totalMonths += 1

        change = profloss - previousprofloss
        if totalMonths != 1:
            changes.append(change)
        if change > greatestIncrease:
            greatestIncrease = change
            highestMonth = date
        if change < greatestDecrease:
            greatestDecrease = change
            lowestMonth = date

        previousprofloss = profloss

avgChange = int(round(sum(changes)/len(changes), 2))
#avgMonthlyProfit = int(round(totalProfit/totalMonths, 0))

data = f"""
Total Profit: ${totalProfit}
Total Months: {totalMonths}
Average Monthtly Change: ${avgChange}
Greatest Increase: {highestMonth}, ${greatestIncrease}
greatest Decrease: {lowestMonth}, ${greatestDecrease}"""
print(data)

output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(data)
