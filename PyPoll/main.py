#PyPoll Code
#Python Script that analyzes the records to calculate values

#Bring in libraries
import os
import csv

#variables
TotalVotes= 0
Candidates = []
PreviousCandidate = 0

#Read in csv file
election_data = os.path.join("Resources","election_data.csv")


# Read in the CSV file
with open(election_data , "r") as data:

    csvreader = csv.reader(data, delimiter=',')
    #skip the header row
    header = next(csvreader)

#loop through the file to set up counters/calcs
    for each in csvreader:

        #counter for total Votes
        TotalVotes+=1

        #If statement for the total candidates list, if the current row is not in the Candidates list, add it, else dont add it
        if str(each[2]) not in Candidates:
            TotalCandidates = str(each[2])
            Candidates.append(TotalCandidates)
        PreviousCandidate = str(each[2])

    print(TotalVotes)
    print(Candidates)
   
    #print("Financial Analysis")
    #print(f"Total Months: {TotalMonths}")
    #print(f"Total: ${NetTotal}")
    #print(f"Average Change: ${AveragePLChange}")
    #print(f"Greatest Increase in Profits: {Months[MaxMonthIndex]} (${MaxPLChange})")
    #print(f"Greatest Decrease in Profits: {Months[MinMonthIndex]} (${MinPLChange})")


#Export to text file
    #Datatext = open("PyBankData.txt", "w")
    #print("Financial Analysis", file=Datatext)
    #print(f"Total Months: {TotalMonths}", file=Datatext)
    #print(f"Total: ${NetTotal}", file=Datatext)
    #print(f"Average Change: ${AveragePLChange}", file=Datatext)
   # print(f"Greatest Increase in Profits: {Months[MaxMonthIndex]} (${MaxPLChange})", file=Datatext)
    #print(f"Greatest Decrease in Profits: {Months[MinMonthIndex]} (${MinPLChange})", file=Datatext)
   # Datatext.close()