import datetime
''' imported the date time module so that the Due column in the text file can be updated.'''
f = open("Database.txt" , "r")
y = open("Logfile.txt" , "a")
''' The code below is for the dates of today and the future so that it can be updated on the database and the logfile'''
tdelta = datetime.timedelta(days = 21)
tday = datetime.date.today()
today = str(tday)
due_date= str(tday + tdelta)


'''Asks for ID number and the book that has been taken out gets its status updated.
If a book has already been taken out by a user, an error message is retrieved telling the user that
the book is no longer available and to try again later
First - ID is checked of the person and if it is a 4 digit code
Second - the book ID is entered and then that book ID is searched in database.txt to see if it is present
if the book is present then the second to last character is looked up in that line
if that character is a "-", then the book can be removed and the program continues
otherwise an errror message is given to the user'''

while True:
 inputID = int(input("Please enter your user id:"))
 if 999<inputID<10000:
    a = input("Which book would you like to checkout? Please enter the id number:")
    databaseLines = f.readlines()
    for i in range (1,24):
        currentLine = databaseLines[i]
        bookID = currentLine[0:2]
        checkAvailable = databaseLines[i]
        if bookID == a:
            checkAvailable = checkAvailable[-2]
            if checkAvailable == "-":
                databaseLines[i] = bookID+'\tBook_'+bookID+'\t\tAuthor_'+bookID+'\tN\t\t' +due_date+ '\n'
                print(databaseLines[0])
                print(databaseLines[i])
                f.close()
                f = open("Database.txt" , "w")
                f.writelines(databaseLines)
                y.write('\n'+bookID+'\tBook_'+bookID+'\t\tAuthor_'+bookID+'\tN\t\t' +today+ '\t\t%d\n' % (inputID))
                break
            else:
                print("That book has been taken out by another user. Please try again later...")
                
    f.close()
    y.close()
 else:
    print("That was not a valid number. Try again...")
    
    
