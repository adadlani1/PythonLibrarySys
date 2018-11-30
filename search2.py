import os

f = open("Database.txt" , "r")
'''opening the text file and assigning each line to a variable so it can be used later in the code
I tried the code from the website you sent me but I dont want the text file being printed.#
I only want each line to be stored as a variable.
The code provided by the website is in green below'''
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
'''filepath = "Database.txt"
with open(filepath) as f:  
   line = f.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = f.readline()
       cnt += 1'''

def menu():
    os.system('menu2.py')

def search():
    n = input("Which book are you looking for? Please enter the book name or ID number.\n")
    '''I also want to know how I would turn this section into a loop so my code
    isnt repetitive and unnecessarily long.
    This code shows what would happen if the book code or name has been enterred'''
    if n == "Book_1" or "01":
        print(line1)
        print(line2)
    elif n == "Book_2" or "02":
        print(line1)
        print(line3)
    elif n == "Book_3" or "03":
        print(line1)
        print(line4)
    elif n == "Book_4" or "04":
        print(line1)
        print(line5)
    elif n == "Book_5" or "05":
        print(line1)
        print(line6)
    elif n == "Book_6" or "06":
        print(line1)
        print(line7)
    elif n == "Book_7" or "07":
        print(line1)
        print(line8)
    elif n == "Book_8" or "08":
        print(line1)
        print(line9)
    elif n == "Book_9" or "09":
        print(line1)
        print(line10)
    elif n == "Book_10" or "10":
        print(line1)
        print(line11)
    elif n == "Book_11" or "11":
        print(line1)
        print(line12)
    elif n == "Book_12" or "12":
        print(line1)
        print(line13)
    elif n == "Book_13" or "13":
        print(line1)
        print(line14)
    elif n == "Book_14" or "14":
        print(line1)
        print(line15)
    elif n == "Book_15" or "15":
        print(line1)
        print(line16)
    elif n == "Book_16" or "16":
        print(line1)
        print(line17)
    elif n == "Book_17" or "17":
        print(line1)
        print(line18)
    elif n == "Book_18" or "18":
        print(line1)
        print(line19)
    elif n == "Book_19" or "19":
        print(line1)
        print(line20)
    elif n == "Book_20" or "20":
        print(line1)
        print(line21)
    elif n == "Book_21" or "21":
        print(line1)
        print(line22)
    elif n == "Book_22" or "22":
        print(line1)
        print(line23)
    elif n == "Book_23" or "23":
        print(line1)
        print(line24)

search()
'''Once a book has been looked up, the code asks the user whether
they would like to lookup the status of another book or go back to the main menu.
Typing "menu" brings up another GUI window.'''
while True:
    x = input("What would you like to do now?\nType:\n'search' to find another book\n'menu' to return to the main menu\n").strip()
    if x == "search":
        search()
    else:
        menu()
        
    

    
