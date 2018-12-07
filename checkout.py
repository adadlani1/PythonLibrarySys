import datetime
import os

''' imported the date time module so that the Due column in the text file can be updated.'''
f = open("Database.txt" , "r")
y = open("Logfile.txt" , "a")
''' The code below is for the dates of today and the future so that it can be updated on the database and the logfile'''
tdelta = datetime.timedelta(days = 21)
tday = datetime.date.today()
today = str(tday)
due_date= str(tday + tdelta)

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

while True:
 f.close()
 f = open("Database.txt", "r")
 y = open("Logfile.txt" , "a")
 inputID = int(input("Please enter your user id:"))
 if 999<inputID<10000:
    a = input("Which book would you like to checkout? Please enter the id number:")
    databaseLines = f.readlines()
    numOfBooks = len(databaseLines)
    databaseLines2 = [i.split(',') for i in databaseLines]
    for i in range (1,numOfBooks):
        book = databaseLines2[i]
        bookID = book[0]
        checkAvailable = book[3]
        titleElement = databaseLines2[0]
        if bookID == a:
            if checkAvailable == "Y":
                book[3] = "N"
                book[4] = inputID
                book[6] = due_date
                print(book)
                databaseLines2[i] = book
                print(databaseLines2)
                print("The book, '"+book[1] + "', is due on "+due_date)
                f.close()
                '''f = open("Database.txt", "w")
                f.close'''
                f = open("Database.txt", "a")
                for q in databaseLines2:
                    print(', '.join(databaseLines2[i]))

                break
            else:
                print("That book has been taken out by another user. Please try again later...")
                break

 else:
    print("That was not a valid number. Try again...")
    break
 f.close()
 y.close()


 
