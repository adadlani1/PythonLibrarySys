import datetime
import os
# import datetime and open the database to be read
databaseFileopen = open("Database.txt", "r")

# find the dates of today and the date in 365 days

tdelta = datetime.timedelta(days = 365)
tday = datetime.date.today()
weedDate = (tday + tdelta)

'''conversion of date in database from str to datetime.
allows me to compare the two dates
if the date the book was last removed is the same or is greater than the todays date,
the program will print the book ID, name, author and the date last removed.'''
def main():
    format = "%Y-%m-%d"
    weedingLines = databaseFileopen.readlines()
    for i in range(1,24):
        currentLine = weedingLines[i]
        lastReturned = currentLine[36:47]
        datetimeLastReturned = datetime.datetime.strptime(lastReturned, format)
        datetimeLastReturned = datetimeLastReturned.date()
        if datetimeLastReturned >= weedDate:
            print("Here is a list of all books in the library:")
            print(weedingLines[0])
            print(currentLine)
        else:
            print("Book_% has been removed within the last year" % i)


main()


secondInput = input("If you would like to return to the menu, type 'menu'").lower().strip()

while True:
    if secondInput == "menu":
        menu()
    else:
        print("What you entered is not an option. Please try again...")
