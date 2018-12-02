import os

f = open("Database.txt" , "r")

def menu():
    os.system('menu.py')

def search():
    a = input("Which book would you like to search for? Please enter the id number:")
    databaseLines = f.readlines()
    for i in range (1,24):
        currentLine = databaseLines[i]
        bookID = currentLine[0:2]
        checkAvailable = databaseLines[i]
        if bookID == a:
            print(databaseLines[0])
            print(databaseLines[i])
search()

'''Once a book has been looked up, the code asks the user whether
they would like to lookup the status of another book or go back to the main menu.
Typing "menu" brings up another GUI window.'''


while True:
    x = input("What would you like to do now?\nType:\n'search' to find another book\n'menu' to return to the main menu\n").strip().lower()
    if x == "search":
        search()
    elif x ==  "menu":
        menu()
    else:
        print("What you enterred is not an option. Please try again...")
        
    

    
