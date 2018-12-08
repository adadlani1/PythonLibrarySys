# import miscellaneous operating system interfaces and datetime module

import os
import datetime

# open all of the files that are going to be used in this system

databaseFileopen = open("Database.txt", "r")
logfileOpen = open("Logfile.txt", "a")

# the days that will be used in the system will be calculated

tdelta = datetime.timedelta(days=21)
tday = datetime.date.today()
today = str(tday)
due_date = str(tday + tdelta)


'''the main() function is the main body of code that uses a 4 digit user ID to access the system
The lines in the database.txt file get turned into a list of lists where each book is an element
book is the book depending on the ID number entered. 
The availability, ID number and due date reverts back to it original state 
so that the book can be taken out once again
A message is also displayed after the elements have been altered saying that the book has been returned
If wrong ID is entered, an error message is displayed'''


def main():

 inputID = int(input("Please enter your user ID:"))
 if 999 < inputID < 10000:
     returnBookIDnum = input("Which book would you like to return? Please enter the id number:")
     databaseFileopen = open("Database.txt", "r")
     databaseLines = databaseFileopen.readlines()
     numOfBooks = len(databaseLines)
     databaseLines2 = [i.split(',') for i in databaseLines]
     for i in range(1, numOfBooks):
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
            print("The book, '" + book[1] + "', has been returned")
            break
        elif checkAvailable == "Y":
            print("This book is still available. Please try again")
            break
     databaseFileopen.close()
 else:
     print("That is an invalid user ID. Please try again...")


# function for the program to open the main menu
'''this function is to reopen the menu.py so that the librarian can perform another action'''
def menu():
    os.system('menu.py')
# function called main is run


'''this is a set of code that will only take place if the script is opened separately but will not if the file is 
imported'''


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