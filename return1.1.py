import os

f = open("Database.txt", "r")
y = open("Logfile.txt", "a")

def backtoMenu():
    os.system('menu2.py')

while True:
    inputID = int(input("Please enter your user ID:"))
    if 999<inputID<10000:
     a = input("Which book would you like to return? Please enter the id number:")
     databaseLines = f.readlines()
     for i in range (1,24):
        currentLine = databaseLines[i]
        bookID = currentLine[0:2]
        checkAvailable = databaseLines[i]
        print(checkAvailable)
        if bookID == a:
            checkAvailable = checkAvailable[-1]
            if checkAvailable == "0" or "1" or "2" or "3" or "4" or "5" or "-":
                print(databaseLines[0])
                print(databaseLines[i])
            
        else:
            print("This book is still available. Please try again")
            break
