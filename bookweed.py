# Written by Anmol Dadlani
# 6th December 2018

import os

'''main function used to count the number of times the book ID appears in logfile
   if book ID appears in logfile 10 or more times, the system suggests that the book is in high demand
   however, if it is less than 10 but greater than 0, the librarian should consider 
   removing the book if the number of times the book appears is 0, it is suggested that the 
   book should definitely be removed'''


def menu():
    os.system('menu.py')


def main():

    logFileopen = open("Logfile.txt", "r")
    weedBook = input("Enter the book ID for information regarding weeding:")
    weedingLines = logFileopen.readlines()
    # turns the text file into a list with n number of elements
    numOfBooks = len(weedingLines)
    # finds the number of elements in the list
    weedingLines2 = [novel.split('{') for novel in weedingLines]
    # forms a list of lists where each list is a different book
    count = 0

    for novel in range(1, numOfBooks-1):
        # uses the range from the 1 to the second to last element in the list of lists
        book = weedingLines2[novel]
        # depending on what number the for loop is on, it will save the list in book variable
        bookID = book[0]
        bookName = book[1]
        # finds the nth element of the list and saves them under a specific variable

        if weedBook == bookID:
            # input ID needs to equal the ID of the book
            count = count + 1
            # count is increased by 1 for every time a specific book is present

    if count >= 10:
        print(bookName+" is in high demand, do not remove.")
    elif 0 < count < 10:
        print(bookName + " is not in high demand, "
                         "please consider removing it to make space for new books.")
        removeBook = input("Would you like to remove this book?:").lower().strip()

        if removeBook == "yes":
            databaseFileOpen = open("Database.txt", "r")
            databaseLines = databaseFileOpen.readlines()
            databaseLines2 = [novel.split('{') for novel in databaseLines]
            numOfBooks = len(databaseLines)
            # data in database is changed into a list of lists where each list is equal to a book

            for novel in range(1, numOfBooks):
                # for loop for the first book to the last
                book = databaseLines2[novel]
                # making a variable equal to the ith list of the list of lists
                bookID = book[0]
                # first element is the ID of the book
                checkAvailable = book[3]

                if bookID == weedBook and checkAvailable == "Y":
                    del databaseLines[novel]
                    databaseFileOpen.close()
                    joinDatabase = '{'.join(databaseLines)
                    databaseFileReOpen = open("Database.txt", "w")
                    databaseFileReOpen.write(joinDatabase)
                    print("The book has been removed")
                elif checkAvailable == "N":
                    print("The book is out on loan at the moment. "
                          "Try again when it has been returned")

    elif count == 0:
        print(weedBook+" is a book no one wants to checkout, "
                       "this book will now be automatically removed")
        databaseFileOpen = open("Database.txt", "r")
        databaseLines = databaseFileOpen.readlines()
        databaseLines2 = [i.split('{') for i in databaseLines]
        numOfBooks = len(databaseLines)
        # data in database is changed into a list of lists where each list is equal to a book

        for novel in range(1, numOfBooks):
            # for loop for the first book to the last
            book = databaseLines2[novel]
            # making a variable equal to the ith list of the list of lists
            bookID = book[0]
            # first element is the ID of the book
            checkAvailable = book[3]

            if bookID == weedBook and checkAvailable == "Y":
                del databaseLines[novel]
                databaseFileOpen.close()
                joinDatabase = '{'.join(databaseLines)
                databaseFileReOpen = open("Database.txt", "w")
                databaseFileReOpen.write(joinDatabase)
                print("The book has been removed")

    logFileopen.close()


if __name__ == "__main__":

    while True:
        main()
        secondInput = input("If you would like to return to the menu, type 'menu'"
                            "\nOr to find another book, type 'weed'\n").lower().strip()

        if secondInput == "menu":
            menu()
        elif secondInput == "weed":
            main()
        else:
            print("What you entered is not an option. Please try again...")
