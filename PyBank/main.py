# Modules
import os
import csv

budget_csv = os.path.join('budget_data.csv')



# Open the CSV
with open(budget_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    next(csvreader)

    #create lists
    dif_list=[]   
    prof_loss=[]
    #set count to 0
    total=0
    datecount=0
    #loop through rows of csv
    for rows in csvreader:
        total += float(rows[1])
        datecount += 1
        prof_loss.append(rows[1])
    #index prof_loss list
    prof_loss_list= range(0,len(prof_loss)-1)

    #find differences and add to list
    for i in prof_loss_list:
        dif_list.append(float(prof_loss[i+1])-float(prof_loss[i]))
        
    #find average of differences
    avg_dif=sum(dif_list)/datecount
    maximum = max(dif_list)
    minimum = min(dif_list)
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(datecount)) 
    print("Total: " + str(total))
    print("Average Change: " + str(avg_dif))
    print("Greatest Increase in Profits: " + str(maximum))
    print("Greatest Decrease in Profits: " +str(minimum))

    #print(prof_loss)
    #print(dif_list)


    