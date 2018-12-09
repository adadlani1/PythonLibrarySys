import datetime
import os

''' imported the date time module so that the Due column in the text file can be updated.

f = open("Database.txt", "r")
y = open("Logfile.txt", "a")'''

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
 # function called main
 while True:
    # while loop that continuously runs this function until it is broken
    databaseFileOpen = open("Database.txt", "r")
    logFileOpen = open("Logfile.txt", "a")
    # files are opened in read format
    inputID = int(input("Please enter your user id:"))
    # user is asked to enter their ID number
    if 999 < inputID < 10000:
        # user's ID is checked whether if it is valid
        a = input("Which book would you like to checkout? Please enter the name:")
        # user is asked to enter the name of the book they would like to checkout
        databaseLines = databaseFileOpen.readlines()
        # the contents of the database.txt is turned into one list with each element being a book
        numOfBooks = len(databaseLines)
        # number of books is determined from the number of elements in the list
        databaseLines2 = [i.split('{') for i in databaseLines]
        # the list is split into a list of lists. This is for alteration of text in database.txt
        databaseLines3 = [i.split('{') for i in databaseLines]
        # the list is split into a list of lists. This is for alteration of text in logfile.txt
        for i in range(1, numOfBooks):
            # for loop for looking through each book
            book = databaseLines2[i]
            logFile = databaseLines3[i]
            # book and logFile select a list and this list contains information for one book
            bookName = book[1]
            # looks up the second element which is the name of the book
            checkAvailable = book[3]
            # looks at the fourth element of book information
            if bookName == a:
                # if the input from user matches the ID that is present in the database, then this function takes place
                if checkAvailable == "Y":
                    # if fourth element of the book is equal to Y then it means it is available
                    # and the user can take it out
                    book[3] = "N"
                    # fourth element is changed to N as it has been removed from the library
                    book[4] = str(inputID)
                    # element 5 is changed to the ID of the user
                    book[5] = due_date
                    # element 6 is changed to the due date so when the text file is accessed,
                    # it states when the book should be returned by
                    del logFile[5:7]
                    # 6th element to the 8th element is deleted
                    logFile[3] = str(inputID)
                    # fourth element is changed to the ID of the user
                    logFile[4] = today
                    # 5th element is changed to today's date as it is the day the book was removed from the library
                    logFile.append('\n')
                    # new line is appended to the end so the next book in the logfile starts on a new line
                    databaseLines2[i] = book
                    # the ith element in the list of lists is overwritten so it can be saved into the database.txt file
                    print("The book, '"+book[1] + "', is due on "+due_date)
                    # this tells the user that the book has been removed and is due on a specific date
                    databaseFileOpen.close()
                    # database file is closed
                    databaseFileOpen = open("Database.txt", "w")
                    # database file is reopened but to be written
                    for line in databaseLines2:
                        # for loop for turning the list of lists into a list
                        recordString = '{'.join(line)
                        # lines are joined together with { between each element
                        databaseFileOpen.write(recordString)
                        # it is finally written to the database file and saved
                        joinlogFile = '{'.join(logFile)
                        # same process as before but for the logfile
                    logFileOpen.write(joinlogFile)
                    # written in the logfile and saved
                    break
                else:
                    print("That book has been taken out by another user. Please try again later...")
                    # when system searches in the book list and finds the element not to be Y then returns
                    # the book is not available
                    break

    else:
        print("That was not a valid number. Try again...")
        # if a 4 digit number has not been entered this error message is displayed
    databaseFileOpen.close()
    logFileOpen.close()


while True:
    # while loop for the whole script to continuously run
    main()
    # main function is run once
    x = input("What would you like to do now?\nType:\n'checkout' to remove another book\n'menu' to return to the main menu\n").strip().lower()
    # user is asked if they would like to checkout another book or return to the menu for another function
    if x == "checkout":
        # if checkout is entered, the main function is run once again
        main()
    elif x == "menu":
        # if menu is entered, GUI for menu is opened
        backtoMenu()
    else:
        # anything else entered, an error message is given
        print("What you entered is not an option. Please try again...")
