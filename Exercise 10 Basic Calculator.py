firstNumber = float (input("Input First Number "))
secoNumber = float (input("Input seco Number "))
operator = input("/,*,+,-")
if operator == "/" :
    print ("Result :",firstNumber/secoNumber)
elif operator == "*" :
    print ("Result :",firstNumber*secoNumber)
elif operator == "+" :
    print ("Result :",firstNumber+secoNumber)
elif operator == "-" :
    print ("Result :",firstNumber-secoNumber)
else :
    print("Hi")
