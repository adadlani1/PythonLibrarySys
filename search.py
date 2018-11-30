first = input("Hello, what would you like to do?\nType 'list' for list of all books\n'search' to find a specific book\n'renew' to renew loaned books\n")
f = open("Database.txt" , "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
line5 = f.readline()
line6 = f.readline()
line7 = f.readline()
line8 = f.readline()
line9 = f.readline()
line10 = f.readline()
line11 = f.readline()
line12 = f.readline()
line13 = f.readline()
line14 = f.readline()
line15 = f.readline()
line16 = f.readline()
line17 = f.readline()
line18 = f.readline()
line19 = f.readline()
line20 = f.readline()
line21 = f.readline()
line22 = f.readline()
line23 = f.readline()
line24 = f.readline()
f.close()
            
while True:
    
    if first == "list":
        f = open("Database.txt" , "r")
        if f.mode == "r":
            contents = f.read()
            print(contents)
            break
    elif first == "search":
        n = input("Which book are you looking for?")
        if n == "Book_1":
            print(line1)
            print(line2)
        elif n == "Book_2":
            print(line1)
            print(line3)
        elif n == "Book_3":
            print(line1)
            print(line4)
        elif n == "Book_4":
            print(line1)
            print(line5)
        elif n == "Book_5":
            print(line1)
            print(line6)
        elif n == "Book_6":
            print(line1)
            print(line7)
        elif n == "Book_7":
            print(line1)
            print(line8)
        elif n == "Book_8":
            print(line1)
            print(line9)
        elif n == "Book_9":
            print(line1)
            print(line10)
        elif n == "Book_10":
            print(line1)
            print(line11)
