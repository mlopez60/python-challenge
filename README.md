# python-challenge
Pybank and Pypoll project:

These two projects involved using the information we learned in Week 3 of the Python Module. 

Much of this could be simplified using Pandas but since we are currently learning that in Week 4, I figured I would do this without those tools as practice. 

Both these projects shared similiarties: 
Begin with calling in/ setting up the csv files to read in data
Performing Various counts on said data to answer the questions
Printing out data to txt files

PyBank: 
The trick for this one was to set up new lists with the data to refer to later when running the calculations.
The new lists were used to store profit and loss difference for each month and then using said list to find the average, max, and min. 

PyPoll: 
This was similar to the previous one but I found it a bit trickier in terms of having the vote data tie in to the candidates
I got around this by setting up a for loop that used a counter to update a dictionary that contained the candidate names. 
My next issue was then figuring out how to get the data to print properly. 
Using list comprehensions and f strings, I was able to extract the data from my dictionary in the proper format. 

I feel like PyPoll has an easier way to accomplish this but I was unsure and feel like I may have complicated things even though I was able to get it to give me the results I was looking for. 

