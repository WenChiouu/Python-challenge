import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

total_months = 0
total = 0
current_profit_loss = 0 
previous_profit_loss = 0
runningAvg = 0
avg = 0
count = 0 
date = 0

running_increase = 0
running_decrease = 0
previous_increase = 0
previous_decrease = 0
current_highest_increase = 0
current_lowest_increase = 0

current_highest_month = ""
current_lowest_month = ""

netchange = []


def runningTotal2(current_profit_loss, previous_profit_loss): 
    difference = current_profit_loss - previous_profit_loss
    return difference 


with open(budget_csv) as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',') 
    csv_header = next(csvReader)
   # csv_header2 = next(csvReader)
        
    for row in csvReader:
            if len(row) > 0 :
                total_months += 1    
                total = total + int(row[1])
                # first line
                if current_profit_loss == 0: #which it is 
                    current_profit_loss = current_profit_loss + int(row[1]) # 0 + 1088983
                    #runningAvg = runningAvg + runningTotal(current_profit_loss, previous_profit_loss) # first line 1088893 - 0 =  WHAT 
                    previous_profit_loss = current_profit_loss #prev is now 1088893
                    # current_profit_loss = 1088893
                    # previous_profit_loss = 1088983
                    # runningAvg = 0

                else: #second line onward for average change
                    current_profit_loss = 0
                    current_profit_loss = current_profit_loss + int(row[1]) # second line 
                    runningAvg = runningAvg + runningTotal2(current_profit_loss, previous_profit_loss) # prev + current / n

                    # netchange.append(running_increase)
                    
                    # avg = runningAvg/(total_months-1) # average change
                    avg = runningAvg/(total_months-1) # average change

                    running_increase = runningTotal2(current_profit_loss, previous_profit_loss)
                    previous_profit_loss = current_profit_loss # average change                      

                    # compare if current difference > previous difference 
                    if running_increase > 0 and running_increase > previous_increase: 
                        previous_increase = running_increase                        
                        current_highest_increase = running_increase # current_highest_increase updated 
                        current_highest_month = row[0]
                    elif running_increase < 0 and running_increase <previous_decrease:
                         previous_decrease = running_increase
                         current_lowest_increase = running_increase
                         current_lowest_month = row[0]


print(f"Financial Analysis")
print(f"----------------------------")                                                        
print(f"Total Months: {total_months}")
print(f"Total : ${total}")
print(f"Average Change : ${avg:.2f}")
print(f"Greatest Increase in Profits: {current_highest_month} (${current_highest_increase})") # ($1862002)
print(f"Greatest Decrease in Profits: {current_lowest_month} (${current_lowest_increase})") # ($-1825558)
