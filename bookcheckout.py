'''Written by Anmol Dadlani
    4th December 2018'''

import datetime
import os

''' imported the date time module so that the Due column in the text file can be updated.'''


''' The code below is for the dates of today and the future so that it can be updated on the database and the logfile'''

tdelta = datetime.timedelta(days=21)
tday = datetime.date.today()
# today's date
today = str(tday)
# today's date but in a string format so it can be written into the text files
due_date = str(tday + tdelta)
# date in the future which will be the date the book needs to be returned by

'''function that opens the menu.py file'''


def backtoMenu():
    os.system('menu.py')


'''Asks for ID number and the book that has been taken out gets its status updated.
If a book has already been taken out by a user, an error message is retrieved telling the user that
the book is no longer available and to try again later
First - ID is checked of the person and if it is a 4 digit code
Second - the book ID is entered and then that book ID is searched in database.txt to see if it is present
if the book is present then the second to last character is looked up in that line
if that character is a "-", then the book can be removed and the program continues
otherwise an error message is given to the user'''

def main():

    while True:
        databaseFileOpen = open("Database.txt", "r")
        logFileOpen = open("Logfile.txt", "a")
        inputID = int(input("Please enter your user id:"))

        if 999 < inputID < 10000:
            ID = input("Which book would you like to checkout? Please enter the "
                                            "the ID:").strip().upper()
            databaseLines = databaseFileOpen.readlines()
            numOfBooks = len(databaseLines)
            # the number of books is determined
            databaseLines2 = [novel.split('{') for novel in databaseLines]
            databaseLines3 = [novel.split('{') for novel in databaseLines]
            # the list database is turned into a list of lists for both
            # databaseLines2 is for use for the book in database
            # databaseLines3 is for use for the info in logfile

        for novel in range(1, numOfBooks):
            book = databaseLines2[novel]
            logFile = databaseLines3[novel]
            bookID = book[0]
            bookName = book[1]
            checkAvailable = book[3]

            if bookID == ID:

                if checkAvailable == "Y":
                    book[3] = "N"
                    book[4] = str(inputID)
                    book[5] = due_date
                    del logFile[3]
                    del logFile[5:7]
                    logFile[3] = str(inputID)
                    logFile[4] = today
                    # elements of both lists are changed to become updated
                    logFile.append('\n')
                    databaseLines2[novel] = book
                    # databaseLines2 is rewritten with the changed list
                    print("The book, '"+book[1] + "', is due on "+due_date)
                    databaseFileOpen.close()
                    databaseFileReOpen = open("Database.txt", "w")

                    for line in databaseLines2:
                        recordString = '{'.join(line)
                        databaseFileReOpen.write(recordString)
                        joinlogFile = '{'.join(logFile)
                    logFileOpen.write(joinlogFile)
                    # databaseLines2 is a list of lists and this for loop
                    # joins it and forms a list then forms it into a string
                    # finally it is written into the logfile and the database
                    databaseFileReOpen.close()
                    break

                else:
                    print("That book has been taken out by another user. Please try again later...")
                    break

        else:
            print("That was not a valid number. Try again...")

        databaseFileOpen.close()
        logFileOpen.close()
        break


'''This is the test code'''

if __name__ == "__main__":
    while True:
        main()
        x = input("What would you like to do now?\nType:\n'checkout' to remove another book"
                  "\n'menu' to return to the main menu\n").strip().lower()
        if x == "checkout":
            main()
        elif x == "menu":
            backtoMenu()
        else:
            print("What you entered is not an option. Please try again...")
