import os
'''main function used to count the number of times the book ID appears in logfile
   if book ID appears in logfile 10 or more times, the system suggests that the book is in high demand
   however, if it is less than 10 but greater than 0, the librarian should consider removing the book
   if the number of times the book appears is 0, it is suggested that the book should definitely be removed'''

def menu():
    os.system('menu.py')

def main():
    logFileopen = open("Logfile.txt", "r")
    #logfile is opened
    weedBook = input("Enter the book ID for information regarding weeding:")
    # user inputs ID number of book
    weedingLines = logFileopen.readlines()
    # turns the text file into a list with n number of elements
    numOfBooks = len(weedingLines)
    # finds the number of elements in the list
    weedingLines2 = [i.split('{') for i in weedingLines]
    # forms a list of lists where each list is a different book
    count = 0
    for i in range(1, numOfBooks-1):
        # uses the range from the 1 to the second to last element in the list of lists
        book = weedingLines2[i]
        # depending on what number the for loop is on, it will save the list in book variable
        bookID = book[0]
        bookName = book[1]
        # finds the first element of the list which is the book ID
        if weedBook == bookID:
            # input ID needs to equal the ID of the book
            count = count + 1
            # count is increased by 1 for every time a specific book is present
    if count >= 10:
        print(bookName+" is in high demand, do not remove.")
    elif 0 < count < 10:
        print(bookName + " is not in high demand, please consider removing it to make space for new books.")
    elif count == 0:
        print(weedBook+" is a book no one wants to checkout, definitely remove from the library.")
    logFileopen.close()


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
