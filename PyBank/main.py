# Modules
import os
import csv

csvpath = os.path.join('budget_data.csv')

# Import Dependencies
import pandas as pd
# Store filepath in a variable
budget_data = "budget_data.csv"

# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
budget_data_df = pd.read_csv(budget_data, encoding="ISO-8859-1")

# Find number of months
unique_months = budget_data_df["Date"].unique()
total_unique_months = len(unique_months)
print (total_unique_months)

#find total profit
total_profit = budget_data_df["Profit/Losses"].sum()
print(total_profit)
#'${:}'.format(total_profit)


prof_loss=budget_data_df["Profit/Losses"]
print(prof_loss)

difference_list = []
#for i in prof_loss:
    #difference_list.append(prof_loss.iloc[i].subtract(prof_loss.iloc[i+1]))

#print(difference_list)


for i in (1,len(prof_loss)-1):
    firstval=prof_loss[i]
    nextval=prof_loss[i-1]
    difference_list.append(firstval-nextval)
print(difference_list)

print(firstval)
print(nextval)