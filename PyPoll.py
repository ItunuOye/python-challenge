
import os
import csv
from collections import Counter


vote_count = 0
khan = 0
correy = 0
li = 0
otooley = 0


py_poll= "election_data.csv"


votes = []
runners = []


with open(py_poll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)


    for row in csvreader:
        votes.append(row[0])
        runners.append(row[2])


candidate_votes = zip(votes, runners)
all_votes = dict(Counter(runners))


#winner = ""
winner_count = 0


for key, value in all_votes.items():
    if value > winner_count:
        winner_count = value
        winner = key


for row in candidate_votes:
    if row[1] == "Khan":
        khan = khan + 1
    elif row[1] == "Correy":
        correy = correy + 1
    elif row[1] == "Li":
        li = li + 1
    else:
        otooley = otooley + 1


vote_count = len(votes)


khan_r = {"Name": "Khan", "Result": khan, "Percent": round(khan/vote_count,5)*100}
correy_r = {"Name": "Correy", "Result": correy, "Percent": round(correy/vote_count,5)*100}
li_r = {"Name": "Li", "Result": li, "Percent": round(li/vote_count,5)*100}
otooley_r = {"Name": "O'Tooley", "Result": otooley, "Percent": round(otooley/vote_count,5)*100}


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(vote_count) + "")
print("-------------------------")
print(khan_r.get("Name") + ": " + "{:.3f}".format(khan_r.get("Percent")) + "% (" + str(khan_r.get("Result")) + ")")
print(correy_r.get("Name") + ": " + "{:.3f}".format(correy_r.get("Percent")) + "% (" + str(correy_r.get("Result")) + ")")
print(li_r.get("Name") + ": " + "{:.3f}".format(li_r.get("Percent")) + "% (" + str(li_r.get("Result")) + ")")
print(otooley_r.get("Name") + ": " + "{:.3f}".format(otooley_r.get("Percent")) + "% (" + str(otooley_r.get("Result")) + ")")
print("-------------------------")
print("Winner: "+ winner)
print("-------------------------")


text_file = open("Election_Results.txt", "w")
text_file.write("Election Results\n")
text_file.write("-------------------------\n")
text_file.write("Total Votes: " + str(vote_count) + "\n")
text_file.write("-------------------------\n")
text_file.write(khan_r.get("Name") + ": " + "{:.3f}".format(khan_r.get("Percent")) + "% (" + str(khan_r.get("Result")) + ")\n")
text_file.write(correy_r.get("Name") + ": " + "{:.3f}".format(correy_r.get("Percent")) + "% (" + str(correy_r.get("Result")) + ")\n")
text_file.write(li_r.get("Name") + ": " + "{:.3f}".format(li_r.get("Percent")) + "% (" + str(li_r.get("Result")) + ")\n")
text_file.write(otooley_r.get("Name") + ": " + "{:.3f}".format(otooley_r.get("Percent")) + "% (" + str(otooley_r.get("Result")) + ")\n")
text_file.write("-------------------------\n")
text_file.write("Winner: "+ winner + "\n")
text_file.write("-------------------------\n")
text_file.close()
