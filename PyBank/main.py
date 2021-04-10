import os
import csv

bank_csv =os.path.join("Resources","budget_data.csv")

month_change = []
date = []

count = 0
initial_profit = 0
total_profit = 0
total_profit_changes = 0

with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:    
      #Keep track of the number of months.
      count = count + 1 
      #Keeps track of the dates.
      date.append(row[0])
      #Adds the profit per month as it loops through the months.
      total_profit = total_profit + int(row[1])
      #Used to keep track of the change in profit per month.
      endmonth_profit = int(row[1])
      monthly_change_profits = endmonth_profit - initial_profit
      month_change.append(monthly_change_profits)
      #Used to find future values. 
      total_profit_changes = total_profit_changes + monthly_change_profits
      initial_profit = endmonth_profit
      #Calculates the average change in profit
      average_change_profits = (total_profit_changes/count)
      #Finds the greatest increase/decrease in profits
      greatest_increase_profits = max(month_change)
      greatest_decrease_profits = min(month_change)
      #Finds the data by correlating the variable for the change to the date. 
      increase_date = date[month_change.index(greatest_increase_profits)]
      decrease_date = date[month_change.index(greatest_decrease_profits)]

    #Print the analysis.
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
#Prints to a text file
with open ('Analysis/Financial_Analysis.txt','w') as text:
    text.write("Financial Analysis" +"\n")
    text.write("----------------------------------------------------------\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("Average Change: " + "$" + str(int(average_change_profits)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increase_date) + " $" + str(greatest_increase_profits) + "\n")
    text.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")

