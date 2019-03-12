import os
import pandas as pd
import csv
py_bank= "/Users/itunuo/Documents/Python_Bank_2/budget_data_IO.csv"

#profit_loss = []
date = []
monthly_change = []
count_month = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
#open as csv file
with open(py_bank, newline="") as csvfile:
    
    #store file information in variable csvreader
    csvreader = csv.reader(csvfile,delimiter=',')
        #print(csvreader). initially used to test if it reads the file. Put a # in front of it after verifying

    #skips the header of the file
    csv_header = next(csvreader)
   
    for row in csvreader:
    # count_month to count the number of months(rows).
        count_month += 1

        #calculate the total profit
        #profit_loss.append(row[1])
        total_profit += int(row[1])

        #store dates for the list
        # To be used when collecting the greatest increase and decrease in profit/loss.
        date.append(row[0])

        #Calculate the average change in profits from month to month.
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #Store monthly changes in a list
        monthly_change.append(monthly_change_profits)

        #total_change_profits = total_change_profits + monthly_change_profits
        total_change_profits += monthly_change_profits
        initial_profit = final_profit
	
	#Calculate the average change in profits
	average_change_profits = (total_profit/count_month)

	#from statistics import mean
	#average_profits = sum(monthly_change)/count_month
	#Find the max and min change in profits and the corresponding dates these changes 	were observed
	greatest_increase = max(monthly_change)
	greatest_decrease = min(monthly_change)
	increase_date = date[monthly_change.index(greatest_increase)]
	decrease_date = date[monthly_change.index(greatest_decrease)]

	#print("Average Change: " + "$" + str(int(average_change_profits)))
	#print("Average Change: " + "$" + str(round(mean(average_change_profits))))
	print("Financial Analysis")
	print("----------------------------------------------------------")
	print("Total Months: " + str(count_month))
	print("Total Profits: " + "$" + str(total_profit))
	print("Average Change: " + "$" + str(int(average_change_profits)))
	print("Greatest Increase in Profits: " + str(increase_date) + " ($" + 			str(greatest_increase) + ")")
	print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + 		     str(greatest_decrease)+ ")")
	print("----------------------------------------------------------")
	print("test1 " + str(total_change_profits))