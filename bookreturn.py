''' Written by Anmol Dadlani
    4th December 2018'''

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


'''the main() function is the main body of code that uses a 4 digit user ID to
access the system
The lines in the database.txt file get turned into a list of lists where each
book is an element
book is the book depending on the ID number entered. 
The availability, ID number and due date reverts back to it original state 
so that the book can be taken out once again
A message is also displayed after the elements have been altered saying
that the book has been returned
If wrong ID is entered, an error message is displayed'''


def main():

    inputID = int(input("Please enter your user ID:"))

    if 999 < inputID < 10000:
        returnBookIDnum = input("Which book would you like to return?"
                                                      " Please enter the id number:")
        # user is asked what book they would like to return
        databaseFileopen = open("Database.txt", "r")
        databaseLines = databaseFileopen.readlines()
        # data in database is turned into a list with each element being a book
        numOfBooks = len(databaseLines)
        # number of books is determined from the number of elements
        # in the list
        databaseLines2 = [novel.split('{') for novel in databaseLines]
        # data in database is changed into a list of lists where each list is
        # equal to a book

        for novel in range(1, numOfBooks):
            book = databaseLines2[novel]
            bookID = book[0]
            checkAvailable = book[3]
            userID = book[4]
            inputIDstr = str(inputID)

            if bookID == returnBookIDnum and inputIDstr == userID:
                # two conditions that need to be met in order for the book to be
                # returned. if the name and ID match with
                # what has been entered, the system will proceed
                # book has to be unavailable (book[3] == N) and userID in database
                # must match ID stored in database
                book[3] = "Y"
                book[4] = "0000"
                book[5] = "----------"
                book[6] = today
                # the database file is updated
                databaseLines2[novel] = book
                # the list is overwritten in the database
                databaseFileopen.close()
                databaseFileReOpen = open("Database.txt", "w")
                # database file is reopened for rewriting all of the books into it

                for line in databaseLines2:
                    # for loop to turn the list of lists into one list
                    recordString = '{'.join(line)
                    # each list is joined together
                    databaseFileReOpen.write(recordString)
                    # it is written into the database file

                print("The book, '" + book[1] + "', has been returned")
                databaseFileReOpen.close()
                # tells user that the book has been returned
                break

            elif checkAvailable =="Y" and bookID == returnBookIDnum:
                print("This book is still available.")
                break

    else:
        print("That is an invalid user ID. Please try again...")

'''this function is to reopen the menu.py so that the librarian can perform another action'''


def menu():
    os.system('menu.py')

'''this is a set of code that will only take place if the script is opened separately but will not if the file is 
imported (test code)'''

if __name__ == "__main__":

    while True:
        main()
        secondInput = input("If you would like to return to the menu,"
                                            " type 'menu', or return another book,"
                                            " type 'return':").lower().strip()

        if secondInput == "menu":
            menu()

        elif secondInput == "return":
            main()

        else:
            print("What you entered is not an option. Please try again...")
