f = open("Database.txt" , "r")
databaseLines = f.readlines()
for i in range (1,24):
    checkAvailable = databaseLines[i]
    checkAvailable = checkAvailable[22:23]

    if checkAvailable == "-":
            
     for i in range(1,24):
        currentLine = databaseLines[i]
        currentLine = currentLine[0:2]
        
        if currentLine == a:
            databaseLines[i] = currentLine+'\tBook_'+currentLine+'\t\tAuthor_'+currentLine+'\tN\t\t' +due_date+ '\n'
            print(databaseLines[0])
            print(databaseLines[i])
            f.close()
            f = open("Database.txt" , "w")
            f.writelines(databaseLines)
            y.write(currentLine+'\tBook_'+currentLine+'\t\tAuthor_'+currentLine+'\tN\t\t' +today+ '\t\t%d\n' % (inputID))
            f.close()
            y.close()
            break
        else:
            print("That book ID is not in our system. Please try again later...")
            break
    else:
        print("This book is not available. Please check later")
