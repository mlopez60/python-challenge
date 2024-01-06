#PyPoll Code
#Python Script that analyzes the records to calculate values

#Bring in libraries
import os
import csv

#variables
TotalVotes= 0
Candidates = []
c={}
Votes = []
Vote = 0
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
        Vote = str(each[2])
        Votes.append(Vote)
        #If statement for the total candidates list, if the current row is not in the Candidates list, add it, else dont add it
        if str(each[2]) not in Candidates:
            TotalCandidates = str(each[2])
            Candidates.append(TotalCandidates)
       
    #for loop to make a dict that takes the candidates and counts occurences
    for each in Votes:
             if each in c:
                c[each] = c[each]+1
             else:
                    c[each]=1
    
    #using the max to find the winner, have to include key=c.get to have it pull the key with highest value, if not it will pull just the max key
    winner = max(c, key=c.get)
  
  #print statements
    print("Election Results")
    print("-------------------------")
    print(F"Total Votes: {TotalVotes}")
    print("-------------------------")
    #list comprehension to print a separate row for each key/value in the dictionary containing voting data
    [print(f" {key.capitalize()}: {round((((value)/TotalVotes)*100),3)}% ({value})") for key,value in c.items()]
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
#Export to text file
    Datatext = open("PyPollData.txt", "w")
    print("Election Results", file =Datatext)
    print("-------------------------", file =Datatext)
    print(F"Total Votes: {TotalVotes}", file =Datatext)
    print("-------------------------", file =Datatext)
    [print(f" {key.capitalize()}: {round((((value)/TotalVotes)*100),3)}% ({value})", file =Datatext) for key,value in c.items()]
    print("-------------------------", file =Datatext)
    print(f"Winner: {winner}", file =Datatext)
    print("-------------------------", file =Datatext)
    Datatext.close()
