# Written by Anmol Dadlani
# 10th December 2018

from tkinter import *

root = Tk()

# defined the functions that are links to the buttons

'''in each of these functions, the .py file is imported and a set of code is run'''


def checkout():

    import bookcheckout

    while True:
        bookcheckout.main()
        # after the main is run, user is asked what they would like to do next
        x = input("What would you like to do now?"
                  "\nType:"
                  "\n'checkout' to remove another book"
                  "\n'menu' to return to the main menu\n").strip().lower()
        # corresponding reply from user runs specfic function in file
        
        if x == "checkout":
            bookcheckout.main()

        elif x == "menu":
            root.withdraw()
            bookcheckout.backtoMenu()

        else:
            print("What you entered is not an option. Please try again...")


def search():

    import booksearch

    while True:
        # while loop which runs the whole system
        booksearch.search()
        # after the main is run, user is asked what they would like to do next
        
        x = input(
            "What would you like to do now?"
            "\nType:"
            "\n'search' to find another book"
            "\n'menu' to return to the main menu\n").strip().lower()
        # corresponding reply from user runs specfic function in file

        if x == "search":
            booksearch.search()
            
        elif x == "menu":
            root.withdraw()
            booksearch.menu()

        else:
            # if another input is made that is not search or menu, program tells
            # the user to try again
            print("What you entered is not an option. Please try again...")


def returnBook():

    import bookreturn

    while True:
        bookreturn.main()
        # after the main is run, user is asked what they would like to do next
        secondInput = input("If you would like to return to the menu, "
                            "type 'menu', or return another book, "
                            "type 'return':").lower().strip()
        # corresponding reply from user runs specfic function in file

        if secondInput == "menu":
            root.withdraw()
            bookreturn.menu()

        elif secondInput == "return":
            bookreturn.main()

        else:
            print("What you entered is not an option. Please try again...")


def weeding():

    import bookweed

    while True:
        bookweed.main()
        # after the main is run, user is asked what they would like to do next
        secondInput = input("If you would like to return to the menu, type 'menu'"
                            "\nOr to find another book, type 'weed'\n").lower().strip()
        # corresponding reply from user runs specfic function in file

        if secondInput == "menu":
            root.withdraw()
            bookweed.menu()

        elif secondInput == "weed":
            bookweed.main()

        else:
            print("What you entered is not an option. Please try again...")


root.title("Anmol's Library System")
root.configure(background='#808080')
# name is given to the window and colour of background is changed

searchButton = Button(root, text = "Search", command = search)
searchButton.place(x = 150, y = 75)
# button is added for its function

canvas = Canvas(root, width=739, height=55, bg = "black")
canvas.pack()
line = canvas.create_line(0, 0, 0, 0)
# added for aesthetics (black line)

checkoutButton = Button(root, text = "Checkout", command = checkout)
checkoutButton.place(x=280, y=75)
# button is added for its function

introMsg = Label(root, text="Hello,\n"
                            "Welcome to Anmol's Library System. "
                            "Please chose from the following what you would like to do"
                            "\nwith your book.", bg='#9932CC', font = ("FIXEDSYS", 12))
introMsg.place(x=0, y=0)
# intro message as soon as GUI window is opened

returnButton = Button(root, text = "Return", command = returnBook)
returnButton.place(x = 425, y = 75)
# button is added for its function

weedingButton = Button(root, text = "Weeding", command = weeding)
weedingButton.place(x = 550, y = 75)
# button is added for its function

root.geometry("739x110")
#size of window
root.mainloop()
