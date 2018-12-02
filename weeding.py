import datetime
import os
# import datetime and open the weedingfile to be read
w = open("Weedingfile.txt", "r")

# find the dates of today and the date in 365 days

tdelta = datetime.timedelta(days = 365)
tday = datetime.date.today()
weedDate= (tday + tdelta)

'''conversion of date in Weedingfile from str to datetime.
allows me to compare the two dates
if the date the book was last removed is the same or is greater than the todays date,
the program will print the book ID, name, author and the date last removed.'''

format = "%Y-%m-%d"
weedingLines = w.readlines()
for line in range (1,24):
    currentLine = weedingLines[line]
    lastRemoved = currentLine[22:32]
    datetimeLastRemoved = datetime.datetime.strptime(lastRemoved, format)
    if datetimeLastRemoved.date() >= weedDate:
        print("Here is a list of all of the books that have not been removed in the last year."
              "These books should be removed to avoid overfilling of the library:")
        print(weedingLines[0])
        print(currentLine)
    else:
        print( "Book_",line,"has been removed within the last year")

secondInput = input("If you would like to return to the menu, type 'menu', or return another book, type 'return':").lower().strip()
while True:
 if secondInput == "menu":
    menu()
 elif secondInput == "return":
    main()
 else:
    print("What you entered is not an option. Please try again...")


