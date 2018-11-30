import datetime
''' imported the date time module so that the Due column in the text file can be updated.'''

f = open("Database.txt" , "r")
y = open("Logfile.txt" , "a")

tdelta = datetime.timedelta(days = 21)
tday = str(datetime.date.today())

due_date= str(tday + tdelta)


'''Asks for ID number and the book that has been taken out gets its status updated.
I need to do the code below for every book. I also need to fill in the
logfile text file to show books each ID has removed'''

while True:
 inputID = int(input("Please enter your user id:"))
 if 999<inputID<10000:
    a = input("Which book would you like to checkout? Please enter the id number:")
    databaseLines = f.readlines()
    for i in range(1,24):
        currentLine = databaseLines[i]
        currentLine = currentLine[0:2]
        if currentLine == a:
            databaseLines[i] = currentLine+'\tBook_'+currentLine+'\t\tAuthor_'+currentLine+'\tN\t\t' +due_date+ '\n'
            print(databaseLines[0])
            print(databaseLines[i])
            f.close()
            f = open("Database.txt" , "w")
            f.writelines(databaseLines)
            y.write(currentLine+'\tBook_'+currentLine+'\t\tAuthor_'+currentLine+'\tN\t\t' +tday+ '\t\t%d\n' % (inputID))
    f.close()
    y.close()
    break   
 else:
    print("That was not a valid number. Try again...")
    
