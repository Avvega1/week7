newphase = "rainstorm"
            #0123456789
            #123456789 - college board version
#create a new variable called shortphrase
#the newphase variable by removing
#the first 3 characters
#the first three characters are "rai"
#the last three characters are "orm"
#substring(string, start, end)    
shortphrase = newphase[3:len(newphase)-3]

#college board version[4:len(newphase)-6]
print(shortphrase)
#explain len(newphase)-3 = 9-3 = 6
#why does it end with 6?
#because the last index is not included