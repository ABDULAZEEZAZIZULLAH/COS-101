#pseudocode
#START
#INPUT students_name
#INPUT daily_transport_cost
#INPUT daily_feeding_cost
#INPUT number_of_days_on_campus
#INPUT other_expense
#CALCULATE transport_total AS daily_transport_cost*number_of_days_on_campus  
#CALCULATE feeding_total AS daily_feeding_cost*number_of_days_on_campus 
#CALCULATE total_money_spent AS transport_total+feeding_total+other_expense
#DISPLAY "STUDENTS WEEKLY EXPENSES"
#DISPALY total_money_spent
#END


#INPUT 
students_name= input("NAME: ")
daily_transport_cost =float(input("DAILY AMOUNT SPENT ON TRANSPORTATION:NAIRA "))
daily_feeding_cost =float(input("DAILY AMOUNT SPENT ON FOOD:NAIRA "))
number_of_days_on_campus = int(input("TOTAL DAYS SPENT ON CAMPUS: "))
other_expense =float(input("OTHER EXPENSES:NAIRA "))
#CALCULATION
transport_total= float(daily_transport_cost*number_of_days_on_campus)
feeding_total=float(daily_feeding_cost*number_of_days_on_campus)
total_money_spent= float(transport_total+feeding_total+other_expense)
#OUTPUT
print ("STUDENTS WEEKLY EXPENSES")
print("====================================")
print ("TOTAL TRANSPORT:NAIRA ",transport_total)
print ("TOTAL FEEDING:NAIRA ",feeding_total)
print ("TOTAL AMOUNT SPENT:NAIRA ",total_money_spent)
print("======================================")

#STUDENTS NAME USES STRING CAUSE ITS A TXT
#DAILY TRANSPORT,DAILY FEEDING AND OTHER EXPENSES ARE ALL AMOUNTS OF MONEY SO IT WILL BE IN FLOAT CAUSE OF IT CAN BE IN DECIMAL
#DAYS SPENT IN CAMPUS WILL BE IN INT CAUSE ITS A WHOLE NUMBER

