# 31.	Check if a number is an Armstrong number.
n=int(input("enter any digit number "))
arms = 0
orginal=n
digits = len(str(n))
while n>0:
    digit = n%10
    arms = arms + (digit ** digits)
    n=n//10
if orginal== arms :
    print ("True")
else :
    print("false")