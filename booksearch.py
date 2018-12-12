# Written by Anmol Dadlani
# 4th December 2018

import os
'''Function that calls menu.py'''

def menu():
    os.system('menu.py')


'''when an input is entered, this function searches the database text file for the name'''
def search():

    inputName = input("Which book would you like to search for? Please enter the name of the book:").strip().upper()
    # user types in name of book they want to look up
    databaseFileOpen = open("Database.txt", "r")
    databaseLines = databaseFileOpen.readlines()
    # database file is turned into a list
    numOfBooks = len(databaseLines)
    # number of elements in the list is determined in order to workout how many books are in the text file
    databaseLines2 = [novel.split('{') for novel in databaseLines]
    # database is turned into a list of lists where each list is a different book

    for novel in range(1, (numOfBooks) ):
        book = databaseLines2[novel]
        # saves a list in the variable
        bookName = book[1]
        # saves the second element in the list which would be the name of the book
        info = databaseLines2[0]
        # this is the list which contains the column headers in the database text files

        if bookName == inputName:

            for columnHeader in range(0, 6):
                print(info[columnHeader], "-", book[columnHeader])


    databaseFileOpen.close()


'''Once a book has been looked up, the code asks the user whether
they would like to lookup the status of another book or go back to the main menu.
Typing "menu" brings up another GUI window. (test code)'''

if __name__ == "__main__":

     while True:
        # while loop which runs the whole system
        search()
        # search function is run first
        furtherOption = input("What would you like to do now?\nType:\n'search' to find another book\n'menu' to return to the main menu\n").strip().lower()
        # user asked what they would like to do next and each input runs a different function

        if furtherOption == "search":
            search()

        elif furtherOption == "menu":
            menu()

        else:
            # if another input is made that is not search or menu, program tells the user to try again
            print("What you entered is not an option. Please try again...")
