f = open("Database.txt" , "r")
a = input("Which book would you like to search for? Please enter the id number:")
databaseLines = f.readlines()
for i in range (1,24):
    currentLine = databaseLines[i]
    bookID = currentLine[0:2]
    checkAvailable = databaseLines[i]
    if bookID == a:
        print(databaseLines[0])
        print(databaseLines[i])
        
