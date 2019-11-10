# Modules
import os
import csv

budget_csv = os.path.join('budget_data.csv')



# Open the CSV
with open(budget_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    next(csvreader)

    #create lists
    prof_loss=[]
    date_list = []
    
    #set count to 0
    total=0
    datecount=0
    maximum=0
    minimum=0
    #loop through rows of csv
    for rows in csvreader:
        total += float(rows[1])
        datecount += 1
        prof_loss.append(rows[1])
        date_list.append(rows[0])
        dif_list=[]   
        #index prof_loss list
        prof_loss_list= range(0,len(prof_loss)-1)
        for i in prof_loss_list:
            dif_list.append(float(prof_loss[i+1])-float(prof_loss[i]))
            if maximum <dif_list[i]:
                maximum = dif_list[i]
                greatest_mo = (rows[0])
            if minimum > dif_list[i]:
                minimum = dif_list[i]
                greatest_dec_mo=(rows[0])
        
    
    #find average of differences
    avg_dif=sum(dif_list)/datecount
  
    #print to terminal
    print("Financial Analysis") 
    print("----------------------")
    print("Total Months: " + str(datecount))
    print("Total: " + "${:.2f}".format(total))
    print("Average Change: " + "${:.2f}".format(avg_dif))
    print("Greatest Increase in Profits: " + greatest_mo + " "+"("+ "${:.0f}".format(maximum))
    print("Greatest Decrease in Profits: "+ greatest_dec_mo + " "+"("+ "${:.0f}".format(minimum) +")"  )

    #print to text file
    print("Financial Analysis" + "\n"+ 
        "----------------------" +"\n"+ 
        "Total Months: " + str(datecount) + "\n" +
        "Total: " + "${:.2f}".format(total) + "\n" +
        "Average Change: " + "${:.2f}".format(avg_dif) + "\n" +
        "Greatest Increase in Profits: " + greatest_mo + " "+"("+ "${:.0f}".format(maximum) +")"+"\n"+
        "Greatest Decrease in Profits: "+ greatest_dec_mo + " "+"("+ "${:.0f}".format(minimum) +")"
        ,  file=open('PyBank.txt', 'w'))



    