#PyBank Code
#Python Script that analyzes the records to calculate values

#Bring in libraries
import os
import csv

#variables
NetTotal = 0
TotalMonths = 0
Months = []
MonthlyChange = []
PLChange = 0
PLprevious = 0
PLCurrent = 0
#Read in csv file
budget_data = os.path.join("Resources","budget_data.csv")


# Read in the CSV file
with open(budget_data , "r") as data:

    csvreader = csv.reader(data, delimiter=',')
    #skip the header row
    header = next(csvreader)

#loop through the file to set up counters/calcs
    for each in csvreader:

        #counter for total months
        TotalMonths+=1

        #counter for the net total
        NetTotal += int(each[1])

        #Track the profit changes for each month; PLchange to take the PL for that month subtracted from the previous month
        #If statement so that the first month PLchange is 0
        if TotalMonths == 1:
            PLCurrent = 0
        else:
            PLCurrent = int(each[1])

        PLChange = PLCurrent - PLprevious
        MonthTracker = str(each[0])
        #adding it into a list to store the changes and months
        MonthlyChange.append(PLChange)
        Months.append(MonthTracker)
    
        #setting the PLprevious variable to be the current one that just finished 
        PLprevious = int(each[1])
   
   #Calculations for getting the average and Max/min using python Sum,Max,Min Functions
    AveragePLChange = (sum(MonthlyChange))/(TotalMonths-1)
    MaxPLChange = max(MonthlyChange)
    MinPLChange = min(MonthlyChange)
    #Variable to find the Max,Min month to correspond with Max,Min value, using index and search in the Month List when printing
    MaxMonthIndex=MonthlyChange.index(MaxPLChange)
    MinMonthIndex=MonthlyChange.index(MinPLChange)
  
    print("Financial Analysis")
    print(f"Total Months: {TotalMonths}")
    print(f"Total: {NetTotal}")
    print(f"Average Change: {AveragePLChange}")
    #print(Months[MaxMonthIndex])
    print(f"Greatest Increase in Profits: {Months[MaxMonthIndex]} ({MaxPLChange})")
    print(f"Greatest Decrease in Profits: {Months[MinMonthIndex]} ({MinPLChange})")
    #print(MaxPLChange)
    #print(Months[MinMonthIndex])
    #print(MinPLChange)


#Export to text file
    