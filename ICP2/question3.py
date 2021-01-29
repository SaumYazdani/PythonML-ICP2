#optional userinputted file name(not use for demonstration purpose). worddictionary set to empty
#openfile opens predetermined file
#filename = input("enter file name")
worddict={}
openfile=open('q3file.txt', 'r')
line=openfile.readlines()
#while there is content in a the line,strip the sentences of spaces, then split the sentence into words
#Next, for each word in the newly splitted list, if there is no value for the key then add a new
#key value to dictionary. if there is a value, check what the old value was, increment it and update the dictionary
while line!="":
    for i in line:
        splitted = i.strip()
        splitted = i.split()
        for i in splitted:
            if worddict.get(i)==None:
                worddict[i]=1
            else:
                prev=worddict.get(i)
                prev+=1
                worddict.update({i:prev})
    line = openfile.readline()
#outfile was set to = user inputted value (simplified for demonstration again)
#outfile = filename
#setting our output file to append. Then going through worddict key,values and outputting them with specific formatting
#finally close the file
out = open('q3file.txt','a')
for i,j in worddict.items():
    out.write('\n' + str(i) + ': ' + str(j))
out.close()
