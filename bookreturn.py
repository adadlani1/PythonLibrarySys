# import miscellaneous operating system interfaces and datetime module

import os
import datetime

#open all of the files that are going to be used in this system

f = open("Database.txt", "r")
y = open("Logfile.txt", "a")
w = open("Weedingfile.txt", "r")

tdelta = datetime.timedelta(days = 21)
tday = datetime.date.today()
today = str(tday)
due_date= str(tday + tdelta)

while True:
    inputID = int(input("Please enter your user ID:"))
    if 999<inputID<10000:
     a = input("Which book would you like to return? Please enter the id number:")
     f = open("Database.txt", "r")
     y = open("Logfile.txt", "a")
     w = open("Weedingfile.txt", "r")
     databaseLines = f.readlines()
     weedingLines = w.readlines()
     for i in range (1,24):
        currentLine = databaseLines[i]
        bookID = currentLine[0:2]
        checkAvailable = databaseLines[i]
        if bookID == a:
            checkAvailable = checkAvailable[-1]
            if checkAvailable == "0" or "1" or "2" or "3" or "4" or "5" :
                print(databaseLines[0])
                print(databaseLines[i])
                databaseLines[i] = bookID+'\tBook_'+bookID+'\t\tAuthor_'+bookID+'\tY\t\t-\n'
                weedingLines[i] = bookID+'\tBook_'+bookID+'\t\tAuthor_'+bookID+'\t'+today+'\n'
                print("The book has been successfully been returned")
                f.close()
                w.close()
                f = open("Database.txt" , "w")
                f.writelines(databaseLines)
                w = open("Weedingfile.txt", "w")
                w.writelines(weedingLines)
                break
            else:
                print("This book is still available. Please try again")
                break
    f.close()
    w.close()
