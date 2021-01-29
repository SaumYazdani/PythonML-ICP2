#asking user for input
userinput = int(input("Enter a non zero whole integer"))
#setting a variable to user's input for use later. setting count to 0
userinputoriginal=userinput
count = 0
#while userinput > 0, check if user input is not divisible by 2(%) - if not, increase count by one and decrement by 1
#if userinput is divisible by 2, divide number in half and increase count by 1
while userinput!=0:
    if userinput % 2 != 0:
        userinput -=1
        count +=1
    else:
        userinput/=2
        count+=1
#output results
print("It takes {} steps to reduce {} to zero".format(count, userinputoriginal))