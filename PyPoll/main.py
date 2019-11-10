# Modules
import os
import csv

election_csv = os.path.join('election_data.csv')

# Open the CSV
with open(election_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    next(csvreader)

    #set count to 0
    votercount=0
    candidate=[]
    candidatepercent=[]
    can0total=0
    can1total=0
    can2total=0
    can3total=0

    #loop to find values
    for rows in csvreader:
        #votercount
        votercount += 1
        #if statement to find votes per candidate
        if rows[2] == 'Khan':
            can0total+=1
        elif rows[2] == 'Correy':
            can1total+=1
        elif rows[2] == 'Li':
            can2total+=1
        elif rows[2] == "O'Tooley":
            can3total+=1
        #candidate list
        if rows[2] not in candidate:
            candidate.append(rows[2])
    #candidate percent list
    candidatepercent.append(can0total/votercount)
    candidatepercent.append(can1total/votercount)
    candidatepercent.append(can2total/votercount)
    candidatepercent.append(can3total/votercount)

    #create dictionary with candidate:% to find winner
    canpercentlist = candidatepercent
    candidatelist = candidate
    winnerdict=dict(zip(candidatelist, canpercentlist))
    #find winner
    winner = max(winnerdict.keys(), key=(lambda k: winnerdict[k]))
    print("Election Results")
    print("----------------------")
    print("Total Votes: " + str(votercount))
    print("----------------------")
    print(candidate[0] + ": " + "{:.2%}".format(candidatepercent[0]) + "(" + str(can0total)+ ")")
    print(candidate[1] + ": " + "{:.2%}".format(candidatepercent[1]) + "(" + str(can1total)+ ")")
    print(candidate[2] + ": " + "{:.2%}".format(candidatepercent[2]) + "(" + str(can2total)+ ")")
    print(candidate[3] + ": " + "{:.2%}".format(candidatepercent[3]) + "(" + str(can3total)+ ")")
    print("----------------------")
    print("Winner:" + winner)
    print("----------------------")



    print("Election Results" + "\n"+ 
        "----------------------" +"\n"+ 
        "Total Votes: " + str(votercount) + "\n" +
        "----------------------" +"\n"+ 
        candidate[0] + ": " + "{:.2%}".format(candidatepercent[0]) + "(" + str(can0total)+ ")"+"\n" + 
        candidate[1] + ": " + "{:.2%}".format(candidatepercent[1]) + "(" + str(can1total)+ ")"+"\n" +
        candidate[2] + ": " + "{:.2%}".format(candidatepercent[2]) + "(" + str(can2total)+ ")"+"\n" +
        candidate[3] + ": " + "{:.2%}".format(candidatepercent[3]) + "(" + str(can3total)+ ")"+"\n" +
        "----------------------" +"\n"+
        "Winner:" + winner +"\n"+
        "----------------------"
        ,  file=open('PyPoll.txt', 'w'))
