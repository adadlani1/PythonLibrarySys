# import miscellaneous operating system interfaces and datetime module

import os
import datetime

# open all of the files that are going to be used in this system

databaseFileopen = open("Database.txt", "r")
logfileOpen = open("Logfile.txt", "a")

# the days that will be used in the system will be calculated

tdelta = datetime.timedelta(days = 21)
tday = datetime.date.today()
today = str(tday)
due_date = str(tday + tdelta)

# loop asks the user to enter their user ID and if the ID is a 4 number ID, program asks which book should be returned


def main():
 inputID = int(input("Please enter your user ID:"))
 if 999<inputID<10000:
     returnBookIDnum = input("Which book would you like to return? Please enter the id number:")
     databaseFileopen = open("Database.txt", "r")
     databaseLines = databaseFileopen.readlines()
     numOfBooks = len(databaseLines)
     databaseLines2 = [i.split(',') for i in databaseLines]
     for i in range (1,numOfBooks):
        book = databaseLines2[i]
        bookID = book[0]
        checkAvailable = book[3]
        userID = book[4]
        inputIDstr = str(inputID)
        titleElement = databaseLines2[0]
        if bookID == returnBookIDnum and inputIDstr == userID:
            book[3] = "Y"
            book[4] = "0000"
            book[5] = "----------"
            book[6] = today
            databaseLines2[i] = book
            databaseFileopen.close()
            f = open("Database.txt", "w")
            for line in databaseLines2:
                recordString = ','.join(line)
                f.write(recordString)
            print("The book, '"+ book[1] + "', has been returned")
            break
        elif checkAvailable == "Y":
            print("This book is still available. Please try again")
            break
     databaseFileopen.close()


# function for the program to open the main menu

def menu():
    os.system('menu.py')
# function called main is run

if __name__ == "__main__":

    main()

    while True:
     secondInput = input("If you would like to return to the menu, type 'menu', or return another book, type 'return':").lower().strip()
     if secondInput == "menu":
        menu()
     elif secondInput == "return":
        main()
     else:
        print("What you entered is not an option. Please try again...")
