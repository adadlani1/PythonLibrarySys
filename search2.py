import os

def menu():
    os.system('menu.py')

def search():
    a = input("Which book would you like to search for? Please enter the name of the book:").strip()
    f = open("Database.txt", "r")
    databaseLines = f.readlines()
    numOfBooks = len(databaseLines)
    databaseLines2 = [i.split(',') for i in databaseLines]
    for i in range (1, (numOfBooks)):
        book = databaseLines2[i]
        bookName = book[1]
        info = databaseLines2[0]
        
        if bookName == a:
            for w in range (0,6):
                print(info[w], "-", book[w])
            
    f.close()



search()


'''Once a book has been looked up, the code asks the user whether
they would like to lookup the status of another book or go back to the main menu.
Typing "menu" brings up another GUI window.'''


while True:
    x = input("What would you like to do now?\nType:\n'search' to find another book\n'menu' to return to the main menu\n").strip().lower()
    if x == "search":
        search()
    elif x == "menu":
        menu()
    else:
        print("What you entered is not an option. Please try again...")
