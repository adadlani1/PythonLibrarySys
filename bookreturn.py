# import miscellaneous operating system interfaces and datetime module

import os
import datetime

#open all of the files that are going to be used in this system

databaseFileopen = open("Database.txt", "r")
logfileOpen = open("Logfile.txt", "a")
weedingFileopen = open("Weedingfile.txt", "r")

# the days that will be used in the system will be calculated

tdelta = datetime.timedelta(days = 21)
tday = datetime.date.today()
today = str(tday)
due_date= str(tday + tdelta)

#loop asks the user to enter their user ID and if the ID is a 4 number ID, program asks which book should be returned
def main(): 
 inputID = int(input("Please enter your user ID:"))
 if 999<inputID<10000:
     returnBookIDnum = input("Which book would you like to return? Please enter the id number:")
     databaseFileopen = open("Database.txt", "r")
     logfileOpen = open("Logfile.txt", "a")
     weedingFileopen = open("Weedingfile.txt", "r")
     databaseLines = databaseFileopen.readlines()
     weedingLines = weedingFileopen.readlines()
     for i in range (1,24):
        currentLine = databaseLines[i]
        bookID = currentLine[0:2]
        checkAvailable = databaseLines[i]
        if bookID == returnBookIDnum:
            checkAvailable = checkAvailable[-2]
            if checkAvailable == "-":
                print("This book is still available. Please try again")
                break
            else:
                print(databaseLines[0])
                print(databaseLines[i])
                databaseLines[i] = bookID+'\tBook_'+bookID+'\t\tAuthor_'+bookID+'\tY\t\t-\n'
                weedingLines[i] = bookID+'\tBook_'+bookID+'\t\tAuthor_'+bookID+'\t'+today+'\n'
                print("The book has successfully been returned")
                databaseFileopen.close()
                weedingFileopen.close()
                databaseFileopen = open("Database.txt" , "w")
                databaseFileopen.writelines(databaseLines)
                w = open("Weedingfile.txt", "w")
                w.writelines(weedingLines)
                break

 databaseFileopen.close()
 weedingFileopen.close()

#function for the program to open the main menu

def menu():
    os.system('menu.py')
#function called main is run
main()
#after main(), program asks user if they would like to return another book or
secondInput = input("If you would like to return to the menu, type 'menu', or return another book, type 'return':").lower().strip()
while True:
 if secondInput == "menu":
    menu()
 elif secondInput == "return":
    main()
 else:
    print("What you entered is not an option. Please try again...")
