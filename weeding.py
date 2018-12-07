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
    numOfBooks = len(weedingLines)
    weedingLines2 = [i.split(',') for i in weedingLines]
    for i in range(1, numOfBooks):
        currentLine = weedingLines[i]
        print(weedingLines2)
        book = weedingLines2[i]
        bookName = book[1]
        lastReturned = currentLine[-12:-2]
        datetimeLastReturned = datetime.datetime.strptime(lastReturned, format)
        datetimeLastReturned = datetimeLastReturned.date()
        if datetimeLastReturned <= weedDate:
            print(bookName, "has not been removed within the last year and needs to be weeded\n")
        else:
            print(bookName, "has been removed within the last year")


main()


secondInput = input("If you would like to return to the menu, type 'menu'").lower().strip()

while True:
    if secondInput == "menu":
        menu()
    else:
        print("What you entered is not an option. Please try again...")
