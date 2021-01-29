#declaring 2 empty lists - one with original user's data and one that will do the cm calculation
heightsdata = []
heightsfinal = []
#asking user for input and setting it to another variable for use later
userq=int(input("How many students?"))
userq1=userq
#asking for user to input a height and decrementing the number they inputted for students.appending heights to list
while userq1!=0:
    userh=float(input("Please enter a height in feet"))
    heightsdata.append(userh)
    userq1-=1
#doing ft to cm calculations on each height in heights data and appending to heightsfinal list
for i in range(userq):
   heightsfinal.append(heightsdata[i]*30.48)
#outputting results
print (heightsfinal)