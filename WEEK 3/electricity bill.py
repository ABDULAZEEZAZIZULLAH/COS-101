customer_name= (input("write your name: "))
energy_used_that_week=(float(input ("the amount of energy used in khw: ")))
rate=(float(input("write the rate: ")))
if rate <= 0:
    print ("invalid input")
elif rate <= 50:
    result=(energy_used_that_week*50)
    print (result)
elif rate >50 and rate <=150:
     result=(energy_used_that_week*75)
     print (result)
elif rate >=150:
     result=(energy_used_that_week*100)
     print (result)
else:
    print ("invalid")
    
