average = float (input("input number of student"))
if average == 90 or average < 100 :
    print ("A")
    if average == 80 or average < 89 :
       print ("B")
    if average == 70 or average < 79 :
       print ("C")
    if average == 60 or average < 69 or average < 60 :
       print ("D")
else :
    print ("F")    
