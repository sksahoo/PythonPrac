loopNum = input("How many no. you wish to check for Odd/Even ")
  
for i in range(int(loopNum)):
    number = int(input("Enter no to check for ODD/EVEN "))
    if number % 2 == 0:
        print("Number {} is even".format(number))
    else :
        print("Number {} is odd".format(number))
