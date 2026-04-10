a=int(input("enter any number betwwn 0 to 40: "))
if (a<0): 
    print("this is a negative number")
elif (a>0):
    if (a<=10):
        print("this number comes Between 1-10")
    elif (a>10 and a <=20):
     print ("this number comes between 10-20")
    elif (a>20 and a <=30):
     print ("this number come in between 20-30")
    elif(a>30 and a <=40):
        print ("this number come in between 30-40")
    else:
      print("number is high than than the 40")

